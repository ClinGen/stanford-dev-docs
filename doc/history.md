# A brief history of Stanford ClinGen

This is the history of ClinGen as best I (Liam Mulhall) know it. It will
probably contain inaccuracies that will need to be corrected. ClinGen was
started in 2013. Matt Wright wasn't part of the initial cohort of people who
worked on ClinGen, but he was part of the second cohort (in 2015). Stanford
ClinGen wasn't originally part of the Gecko Group. Teri Klein absorbed Stanford
ClinGen into her group in 2021.

Our old repository (available to peruse
[here](https://github.com/ClinGen/clincoded)) has Git commits going back to
December 2012.

In January 2022, we published a
[paper](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-021-01004-8)
in Genome Medicine about our effort to re-architect the VCI. There is a
paragraph that describes the history of the VCI:

> The VCI software and product development teams worked alongside the ClinGen
> Variant Curation Interface Task Team to develop the initial platform. This
> product was designed through a user engagement process and VCI v1.0 was
> launched for use in September 2016, with new features developed and released
> monthly. The completely re-architected and updated VCI v2.0 platform was
> launched in December 2020 and is the current production version.

The re-architecture also affected the code in the GCI. The paper is worth
reading, but the summary is that the VCI and GCI use the serverless
architecture. React is used for the front end, and Python is used on the back
end. There's a sentence in the paper that describes the old tech stack:

> The VCI v1.0 \[was\] built following a classical three-tier architecture with
> a web-frontend component (ReactJS), backend business logic layer (Python and
> Pyramid), a split persistence layer containing the state and metadata database
> (PostgreSQL), and search indexes (AWS Elasticsearch).

A [paper](https://pubmed.ncbi.nlm.nih.gov/38663031/) on the GCI is going to be
published in July 2024.
