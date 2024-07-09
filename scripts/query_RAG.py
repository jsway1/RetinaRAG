from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.llamafile import Llamafile
from langchain_community.embeddings import LlamafileEmbeddings
import openai

chroma_path = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

You interpret the following abbreviations automatically: 

AC - anterior chamber, ACIOL – anterior chamber intraocular lens, AFX - air-fluid exchange,
AIDS - acquired immunodeficiency syndrome, AMD - age-related macular degeneration, AP - anterior-posterior, 
APD - afferent pupillary defect, BP - blood pressure, BRVO - branch retinal vein occlusion, 
BSS - balanced salt solution, cc - cubic centimeter, CME – cystoid macular edema, CMV - cytomegalovirus, 
CNV - choroidal neovascularization, cpm – cuts per minute, CSF- cerebrospinal fluid, 
CT - computed tomography, D5W - dextrose 5% in water, DD - disc diameter, DDX - differential diagnosis, 
EBV - Epstein-Barr virus, ERG – electroretinogram, ERM - epiretinal membrane, EUA - examination under anesthesia, 
FAX - fluid-air exchange, FB - foreign body, FDA – Food and Drug Administration, FEVR - familial exudative vitreoretinopathy, 
FTMH – full-thickness macular hole, G – gauge, GA – geographic atrophy, GRT - giant retinal tear, 
HIV - human immunodeficiency virus, HOB - head of bed, HSV - Herpes simplex virus, HZV - Herpes zoster virus, 
ICG - indocyanine green, ILM - internal limiting membrane, IOFB - intraocular foreign body, 
IOL – intraocular lens, IOP – intraocular pressure, IRF- intraretinal fluid, IRH - intraretinal hemorrhage, 
IV - intravenous, LASIK - laser-assisted in situ keratomileusis, LP – light perception, mcg - microgram, 
MH - macular hole, MIVS - microincisional vitrectomy surgery, MRI - magnetic resonance imaging, ms - millisecond,
MVR - microvitreoretinal, mW - milliwatt, NCVH - non-clearing vitreous hemorrhage, NLP - no light perception, 
nm – nanometer, NSAID - nonsteroidal anti-inflammatory drug, NV - neovascularization, NVD – neovascularization of the disc, 
NVI – neovascularization of the iris, OCT - optical coherence tomography, OR - operating room, PCIOL – posterior chamber intraocular lens, 
PCR - polymerase chain reaction, PCV - polypoidal choroidal vasculopathy, PFCL - perfluorocarbon liquid, PI - peripheral iridotomy, 
PPV - pars plana vitrectomy, PRH - preretinal hemorrhage, PRK - photorefractive keratectomy, PRP - panretinal laser photocoagulation, 
PVD - posterior vitreous detachment, PVR - proliferative vitreoretinopathy, RAM - retinal arterial macroaneurysm, 
RD - retinal detachment, RRD - rhegmatogenous retinal detachment, ROP - retinopathy of prematurity, RP - retinitis pigmentosa,
RPE - retinal pigment epithelium, rtPA - recombinant tissue plasminogen activator, SB - scleral buckle, SRF - subretinal fluid, 
SRH - subretinal hemorrhage, TB - tuberculin, TRD - tractional retinal detachment, UGH – uveitis-glaucoma-hyphema, VA - visual acuity, 
VEGF - vascular endothelial growth factor, VH – vitreous hemorrhage, VMT - vitreomacular traction, VR - vitreoretinal, VZV - Varicella Zoster virus

{context}

---

Answer the question based on the above context: {question}

"""

def get_embeddings():
    """
    This function generates the embeddings for the documents. The llamafile is used to generate embeddings.
    
    Input:
    None
    
    Returns:
    embeddings
    """
    embeddings = LlamafileEmbeddings()
    return embeddings


def invoke_llamafile(prompt):
    
    """
    This function interacts with the Llamafile model to get the response.
    
    Input:
    prompt: str
    
    Returns:
    response: str
    """
    client = openai.OpenAI(
        base_url="http://host.docker.internal:8080/v1",
        api_key="sk-no-key-required"
    )
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
            {"role": "system", "content": "You are an experienced vitreoretinal surgeon speaking with trainees. You can answer detailed questions about vitreoretinal surgery concisely and accurately. Keep response length short (within 100 words if possible)"},
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message.content

def query_rag(query_text: str):
    
    """
    This function queries the RAG system. The function takes in a query text and returns the response from the RAG system.
    
    Input:
    query_text: str
    
    Returns:
    response_text: str
    
    """
    # Get the embedding function and search the database
    embedding_function = get_embeddings()
    db = Chroma(persist_directory=chroma_path, embedding_function=embedding_function)

    # Search the database for the most similar chunks, and return the top 3
    results = db.similarity_search_with_score(query_text, k=3)

    # Prepare context text
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Instantiate and use the Llamafile to get the response
    response = invoke_llamafile(prompt)

    # Getting chunk information so we can cite the sources
    #sources = [doc.metadata.get("id", None) for doc, _score in results]
    #formatted_response = f"Response: {response}\nSources: {sources}"

    #print(formatted_response)
    return response    
