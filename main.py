from scripts.createdb import docloader, chunking, get_embeddings, chunk_ids, populate_chromadb
from scripts.query_RAG import get_embeddings, query_rag


def main(query):
  
    chroma_path = "CHROMA_PATH"
    data_path = "DATA_PATH"

  
    PROMPT_TEMPLATE = """
    Answer the question based only on the following context:

    You are an experienced vitreoretinal surgeon speaking with trainees. You can answer detailed questions about vitreoretinal surgery concisely and accurately. Keep response length short (within 100 works if possible)
    You interpret the following abbreviations automatically: 

      AC - anterior chamber, ACIOL – anterior chamber intraocular lens, AFX - air-fluid exchange,
      AIDS - acquired immunodeficiency syndrome, AMD - age-related macular degeneration, AP - anterior-posterior, 
      APD - afferent pupillary defect, BP - blood pressure, BRVO - branch retinal vein occlusion, 
      BSS - balanced salt solution, cc - cubic centimeter, CME – cystoid macular edema, CMV - cytomegalovirus, 
      CNV - choroidal neovascularization, cpm – cuts per minute, CSF- cerebrospinal fluid, 
      CT - computed tomography, D5W - dextrose 5% in water, DD - disc diameter, DDX - differential diagnosis, 
      EBV - Epstein-Barr virus, ERG – electroretinogram, ERM - epiretinal membrane, EUA - examination under anesthesia, 
      FAX - fluid-air exchange, FB - foreign body, FDA – Food and Drug Administration,, FEVR - familial exudative vitreoretinopathy, 
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
      VEGF - vascular endothelial growth factor, VH – vitreous hemorrhage, VMT - vitreomacular traction, VR - vitreoretinal, VZV - Varicella Zoster virus"

      {context}

      ---

      Answer the question based on the above context: {question}

      """

    docs = docloader()
    chunks = chunking(docs)
    populate_chromadb(chunks)
    response = query_rag(query) 
  
    return response
