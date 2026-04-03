from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'includedcc',
     'default_range': 'string',
     'description': 'LinkML Schema for the internal INCLUDE DCC Access Model',
     'id': 'https://includedcc.org/include-access-model',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'include-access-model',
     'prefixes': {'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'cdc_race_eth': {'prefix_prefix': 'cdc_race_eth',
                                   'prefix_reference': 'urn:oid:2.16.840.1.113883.6.238/'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/'},
                  'ig2_biospecimen_availability': {'prefix_prefix': 'ig2_biospecimen_availability',
                                                   'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/'},
                  'ig2dac': {'prefix_prefix': 'ig2dac',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ig2dat': {'prefix_prefix': 'ig2dat',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/'},
                  'ig_dob_method': {'prefix_prefix': 'ig_dob_method',
                                    'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/'},
                  'igcondtype': {'prefix_prefix': 'igcondtype',
                                 'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/'},
                  'includedcc': {'prefix_prefix': 'includedcc',
                                 'prefix_reference': 'https://includedcc.org/include-access-model/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mesh': {'prefix_prefix': 'mesh',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'snomed_ct': {'prefix_prefix': 'snomed_ct',
                                'prefix_reference': 'http://snomed.info/id/'}},
     'see_also': ['https://includedcc.github.io/include-access-model'],
     'source_file': 'src/include_access_model/schema/include_access_model.yaml',
     'title': 'INCLUDE DCC Access Model'} )

class EnumProgram(str, Enum):
    """
    Funding programs relevant to inform operations.
    """
    INCLUDE = "include"
    KF = "kf"
    Other = "other"


class EnumResearchDomain(str, Enum):
    """
    Domains of Research used to find studies.
    """
    Behavior_and_Behavior_Mechanisms = "behavior_and_behavior_mechanisms"
    Congenital_Heart_Defects = "congenital_heart_defects"
    Immune_System_Diseases = "immune_system_diseases"
    Hematologic_Diseases = "hematologic_diseases"
    Neurodevelopment = "neurodevelopment"
    Sleep_Wake_Disorders = "sleep_wake_disorders"
    All_Co_occurring_Conditions = "all_co_occurring_conditions"
    Physical_Fitness = "physical_fitness"
    Other = "other"


class EnumParticipantLifespanStage(str, Enum):
    """
    Stages of life during which participants may be recruited.
    """
    Fetal = "fetal"
    """
    Before birth
    """
    Neonatal = "neonatal"
    """
    0-28 days old
    """
    Pediatric = "pediatric"
    """
    Birth-17 years old
    """
    Adult = "adult"
    """
    18+ years old
    """


class EnumStudyDesign(str, Enum):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    Case_Control = "case_control"
    Case_Set = "case_set"
    Control_Set = "control_set"
    Clinical_Trial = "clinical_trial"
    Cross_Sectional = "cross_sectional"
    FamilySOLIDUSTwinsSOLIDUSTrios = "family_twins_trios"
    Interventional = "interventional"
    Longitudinal = "longitudinal"
    Trial_Readiness_Study = "trial_readiness_study"
    Tumor_vs_Matched_Normal = "tumor_vs_matched_normal"


class EnumClinicalDataSourceType(str, Enum):
    """
    Approaches to ascertain clinical information about a participant.
    """
    Medical_Record = "medical_record"
    """
    Data obtained directly from medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """
    Unknown = "unknown"


class EnumDataCategory(str, Enum):
    """
    Categories of data which may be collected about participants.
    """
    Unharmonized_DemographicSOLIDUSClinical_Data = "unharmonized_demographic_clinical_data"
    Harmonized_DemographicSOLIDUSClinical_Data = "harmonized_demographic_clinical_data"
    Genomics = "genomics"
    Transcriptomics = "transcriptomics"
    Epigenomics = "epigenomics"
    Proteomics = "proteomics"
    Metabolomics = "metabolomics"
    CognitiveSOLIDUSBehavioral = "cognitive_behavioral"
    Immune_Profiling = "immune_profiling"
    Imaging = "imaging"
    Microbiome = "microbiome"
    Fitness = "fitness"
    Physical_Activity = "physical_activity"
    Other = "other"
    Sleep_Study = "sleep_study"


class EnumSubjectType(str, Enum):
    """
    Types of Subject entities
    """
    participant = "participant"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    non_participant = "non_participant"
    """
    An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.
    """
    cell_line = "cell_line"
    """
    Cell Line
    """
    animal_model = "animal_model"
    """
    Animal model
    """
    group = "group"
    """
    A group of individuals or entities.
    """
    other = "other"
    """
    A different entity type- ideally this will be resolved!
    """


class EnumDownSyndromeStatus(str, Enum):
    """
    Down syndrome / chromosome 21 status
    """
    D21 = "d21"
    """
    Disomy 21 (euploid)
    """
    T21 = "t21"
    """
    Trisomy 21 (Down syndrome)
    """


class EnumSex(str, Enum):
    """
    Subject Sex
    """
    Female = "female"
    Male = "male"
    Other = "other"
    Unknown = "unknown"


class EnumRace(str, Enum):
    """
    Participant Race
    """
    American_Indian_or_Alaska_Native = "american_indian_or_alaska_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    More_than_one_race = "more_than_one_race"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_other_pacific_islander"
    Other = "other"
    White = "white"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"
    East_Asian = "east_asian"
    """
    UK only; do not use for US data
    """
    Latin_American = "latin_american"
    """
    UK only; do not use for US data
    """
    Middle_Eastern_or_North_African = "middle_eastern_or_north_african"
    """
    UK only; do not use for US data
    """
    South_Asian = "south_asian"
    """
    UK only; do not use for US data
    """


class EnumEthnicity(str, Enum):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    Hispanic_or_Latino = "hispanic_or_latino"
    Not_Hispanic_or_Latino = "not_hispanic_or_latino"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"


class EnumVitalStatus(str, Enum):
    """
    Descriptions of a Subject's vital status
    """
    Dead = "dead"
    Alive = "alive"


class EnumNull(str, Enum):
    """
    Base enumeration providing null options.
    """
    Unknown = "unknown"


class EnumAssertionProvenance(str, Enum):
    """
    Possible data sources for assertions.
    """
    Medical_Record = "medical_record"
    """
    Data obtained from a medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """


class EnumAvailabilityStatus(str, Enum):
    """
    Is the biospecimen available for use?
    """
    Available = "available"
    """
    Biospecimen is Available
    """
    Unavailable = "unavailable"
    """
    Biospecimen is Unavailable
    """


class EnumSampleCollectionMethod(str):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    pass


class EnumSite(str):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.
    """
    pass


class EnumSpatialQualifiers(str):
    """
    Any spatial/location qualifiers.
    """
    pass


class EnumLaterality(str):
    """
    Laterality information for the site
    """
    pass


class EnumEDAMFormats(str):
    """
    Data formats from the EDAM ontology.
    """
    pass


class EnumEDAMDataTypes(str):
    """
    Data types from the EDAM ontology.
    """
    pass


class EnumFileHashType(str, Enum):
    """
    Types of file hashes supported.
    """
    MD5 = "md5"
    ETag = "etag"
    SHA_1 = "sha1"


class EnumAccessType(str, Enum):
    """
    Types of file access levels.
    """
    Open_Access = "open"
    Controlled_Access = "controlled"
    Registered_tier_Access = "registered"


class EnumExperimentalStrategy(str, Enum):
    """
    Types of sequencing methods.
    """
    Whole_Genome_Sequencing = "wgs"
    RNA_Seq = "rnaseq"
    Whole_Exome_Sequencing = "wxs"
    Methylation = "methlyation"
    Continuous_Long_Reads_WGS = "clr_wgs"
    Proteomics = "proteomics"
    Targeted_Sequencing = "targeted_seq"
    Circular_Consensus_Sequencing_WGS = "ccs_wgs"
    Panel = "panel"
    Circular_Consensus_Sequencing_RNA_Se = "ccs_rnaseq"
    Oxford_Nanopore_Technologies_WGS = "ont_wgs"
    Continuous_Long_Reads_RNA_Seq = "clr_rnaseq"


class EnumAssayCenter(str, Enum):
    """
    Organizations or centers producing raw or harmonized sequencing files.
    """
    The_Broad_Institute = "broad"
    HudsonAlpha_Institute_for_Biotechnology = "hudsonalpha"
    StFULL_STOP_Jude = "stjude"
    Baylor_College_of_Medicine = "baylor"
    The_ChildrenAPOSTROPHEs_Hospital_of_Philadelphia = "chop"
    Other = "other"
    Unknown = "unknown"


class EnumRepository(str, Enum):
    """
    specific drs service used for registration
    """
    Cavatica_DRS = "cavatica"
    NCI_DCF = "dcf"
    Other = "other"


class EnumPlatform(str, Enum):
    """
    names of instrument or platforms used for assay data generation
    """
    Illumina = "illumina"
    PacBio = "pacbio"
    ONT = "ont"
    Illumina_Infinium_HumanMethylationEPICv2 = "illumina_epic"
    Other = "other"
    Unknown = "unknown"



class Record(ConfiguredBaseModel):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Record'})

    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Study(Record):
    """
    Study Metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'study_id': {'identifier': True,
                                     'name': 'study_id',
                                     'range': 'string',
                                     'required': True}},
         'title': 'Research Study'})

    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'StudyMetadata', 'File', 'FileAdmin']} })
    parent_study: Optional[str] = Field(default=None, title="Parent Study", description="""The parent study for this study, if it is a nested study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_title: str = Field(default=..., description="""Full Study Title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_code: str = Field(default=..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_short_name: Optional[str] = Field(default=None, title="Study Code", description="""Short name for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    program: list[EnumProgram] = Field(default=..., title="Program", description="""Funding source(s) for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    funding_source: Optional[list[str]] = Field(default=[], title="Funding Source", description="""The funding source(s) of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: list[Investigator] = Field(default=..., title="Principal Investigator", description="""The Principal Investigator(s) responsible for the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    contact: list[Investigator] = Field(default=..., title="Contact Person", description="""The individual to contact with questions about this record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository']} })
    study_description: str = Field(default=..., title="Study Description", description="""Brief description of the study (2-4 sentences)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website for the Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository', 'Publication']} })
    publication: Optional[list[Publication]] = Field(default=[], title="Publication", description="""Publications associated with this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'Dataset']} })
    acknowledgments: Optional[str] = Field(default=None, title="Acknowledgments", description="""Funding statement and acknowledgments for this study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    citation_statement: Optional[str] = Field(default=None, title="Citation Statement", description="""Statement that secondary data users should use to acknowledge use of this study or dataset. E.g., \"The results analyzed and <published or shown> here are based in whole or in part upon data generated by the INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE) Project <insert accession number(s) and/or study DOI(s)>, and were accessed from the INCLUDE Data Hub and <insert other database(s)>.\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    do_id: Optional[str] = Field(default=None, title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class StudyMetadata(Record):
    """
    Additional features about studies that may not apply to all studies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'data_category': {'multivalued': True,
                                          'name': 'data_category',
                                          'required': True},
                        'study_id': {'identifier': True,
                                     'name': 'study_id',
                                     'required': True}},
         'title': 'Study Metadata'})

    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'StudyMetadata', 'File', 'FileAdmin']} })
    participant_lifespan_stage: list[EnumParticipantLifespanStage] = Field(default=..., title="Participant Lifespan Stage", description="""Focus age group(s) of the study population""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    selection_criteria: Optional[str] = Field(default=None, title="Selection Criteria", description="""Brief description of inclusion and/or exclusion criteria for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    study_design: list[EnumStudyDesign] = Field(default=..., title="Study Design", description="""Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    clinical_data_source_type: list[EnumClinicalDataSourceType] = Field(default=..., title="Clinical Data Source Type", description="""Source(s) of data collected from study participants""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    data_category: list[EnumDataCategory] = Field(default=..., title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata', 'File', 'FileAssay']} })
    vbr: Optional[VirtualBiorepository] = Field(default=None, title="Virtual Biorepository", description="""Information about the study's Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    research_domain: list[EnumResearchDomain] = Field(default=..., description="""Main research domain(s) of the study, other than Down syndrome""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    expected_number_of_participants: int = Field(default=..., title="Expected Number of Participants", description="""Total expected number of participants to be recruited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    actual_number_of_participants: int = Field(default=..., title="Actual Number of Participants", description="""Total participants included at this time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class VirtualBiorepository(Record):
    """
    An organization that can provide access to specimen for further analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Virtual BioRepository (VBR)'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""Name of the institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    contact: list[Investigator] = Field(default=..., title="Contact Person", description="""The individual to contact with questions about this record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website for the Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository', 'Publication']} })
    vbr_readme: Optional[str] = Field(default=None, title="VBR Readme", description="""Instructions for contacting or requesting samples from Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class DOI(Record):
    """
    A DOI is a permanent reference with metadata about a digital object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'do_id': {'identifier': True,
                                  'name': 'do_id',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Digital Object Identifier (DOI)'})

    do_id: str = Field(default=..., title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    bibliographic_reference: Optional[str] = Field(default=None, title="Bibiliographic Reference", description="""Text use to reference this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DOI', 'Publication']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Investigator(Record):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Investigator'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""Name of the institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    investigator_title: Optional[str] = Field(default=None, title="Investigator Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigator']} })
    email: Optional[str] = Field(default=None, title="Email Address", description="""An email address to reach the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigator']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Publication(Record):
    """
    Information about a specific publication.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Publication'})

    bibliographic_reference: Optional[str] = Field(default=None, title="Bibiliographic Reference", description="""Text use to reference this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DOI', 'Publication']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website for the Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository', 'Publication']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Subject(Record):
    """
    This entity is the subject about which data or references are recorded. This includes the idea of a human participant in a study, a cell line, an animal model, or any other similar entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'subject_id': {'identifier': True,
                                       'name': 'subject_id',
                                       'range': 'string',
                                       'required': True}},
         'title': 'Subject'})

    subject_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    subject_type: EnumSubjectType = Field(default=..., title="Subject Type", description="""Type of entity this record represents""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    organism_type: Optional[str] = Field(default=None, title="Organism Type", description="""Organism Type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Demographics(Record):
    """
    Basic participant demographics summary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'subject_id': {'identifier': True,
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'Demographics'})

    subject_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    sex: EnumSex = Field(default=..., title="Sex", description="""Sex of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    race: list[EnumRace] = Field(default=..., title="Race", description="""Race of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    ethnicity: EnumEthnicity = Field(default=..., title="Ethnicity", description="""Ethnicity of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    down_syndrome_status: EnumDownSyndromeStatus = Field(default=..., title="Down Syndrome Status", description="""Down Syndrome status of participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    age_at_last_vital_status: Optional[int] = Field(default=None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics'], 'unit': {'ucum_code': 'd'}} })
    vital_status: Optional[EnumVitalStatus] = Field(default=None, title="Vital Status", description="""Whether participant is alive or dead""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    age_at_first_engagement: Optional[int] = Field(default=None, title="Age at First Participant Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics'], 'unit': {'ucum_code': 'd'}} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class SubjectAssertion(Record):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'assertion_id': {'identifier': True,
                                         'name': 'assertion_id',
                                         'range': 'string',
                                         'required': True}},
         'title': 'Subject Assertion'})

    assertion_id: str = Field(default=..., title="Assertion ID", description="""INCLUDE Global ID for the Assertion""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    subject_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    encounter_id: Optional[str] = Field(default=None, title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    assertion_provenance: Optional[EnumAssertionProvenance] = Field(default=None, title="Assertion Provenance", description="""The original source of this assertion""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    age_at_assertion: Optional[int] = Field(default=None, title="Age at assertion", description="""The age in days of the Subject when the assertion was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'd'}} })
    age_at_event: Optional[int] = Field(default=None, title="Age at event", description="""The age in days of the Subject at the time point which the assertion describes, eg, age of onset or when a measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'Encounter'], 'unit': {'ucum_code': 'd'}} })
    age_at_resolution: Optional[int] = Field(default=None, title="Age at resolution", description="""The age in days of the Subject when the asserted state was resolved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'd'}} })
    concept: Optional[list[str]] = Field(default=[], title="Concept", description="""The structured term defining the meaning of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    concept_source: Optional[str] = Field(default=None, title="Concept Source Text", description="""The source text yielding the standardized concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_concept: Optional[list[str]] = Field(default=[], title="Value concept", description="""The structured term defining the value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_number: Optional[float] = Field(default=None, title="Value Number", description="""The numeric value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_source: Optional[str] = Field(default=None, title="Value Source Text", description="""The source text yielding the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_unit: Optional[str] = Field(default=None, title="Value Units", description="""The structured term defining the units of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_unit_source: Optional[str] = Field(default=None, title="Value Units Source Text", description="""The source text yielding the value's units.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Concept(ConfiguredBaseModel):
    """
    A standardized concept with display information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'concept_curie': {'identifier': True,
                                          'name': 'concept_curie',
                                          'required': True}},
         'title': 'Concept'})

    concept_curie: str = Field(default=..., title="Concept Curie", description="""The standardized curie for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    display: Optional[str] = Field(default=None, title="Display String", description="""The friendly display string of the coded term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })


class Sample(Record):
    """
    A functionally equivalent specimen taken from a participant or processed from such a sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'biospecimen_collection_id': {'description': 'Biospecimen '
                                                                     'Collection '
                                                                     'during which '
                                                                     'this sample was '
                                                                     'generated.',
                                                      'name': 'biospecimen_collection_id'},
                        'sample_id': {'identifier': True,
                                      'name': 'sample_id',
                                      'range': 'string',
                                      'required': True}},
         'title': 'Sample'})

    sample_id: str = Field(default=..., title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'FileAdmin', 'FileAssay']} })
    biospecimen_collection_id: Optional[str] = Field(default=None, title="Biospecimen Collection ID", description="""Biospecimen Collection during which this sample was generated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiospecimenCollection']} })
    parent_sample_id: Optional[str] = Field(default=None, title="Parent Sample ID", description="""Sample from which this sample is derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sample_type: str = Field(default=..., title="Sample Type", description="""Type of material of which this Sample is comprised""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    processing: Optional[list[str]] = Field(default=[], title="Sample Processing", description="""Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    availablity_status: Optional[EnumAvailabilityStatus] = Field(default=None, title="Sample Availability", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    storage_method: Optional[list[str]] = Field(default=[], title="Sample Storage Method", description="""Sample storage method, eg, Frozen or with additives""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_unit: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class BiospecimenCollection(Record):
    """
    A biospecimen collection event which yields one or more Samples.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'biospecimen_collection_id': {'identifier': True,
                                                      'name': 'biospecimen_collection_id',
                                                      'range': 'string',
                                                      'required': True}},
         'title': 'BiospecimenCollection'})

    biospecimen_collection_id: str = Field(default=..., title="Biospecimen Collection ID", description="""Unique identifier for this Biospecimen Collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiospecimenCollection']} })
    age_at_collection: Optional[float] = Field(default=None, title="Age at Biospecimen Collection", description="""The age at which this biospecimen was collected in decimal years.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection'], 'unit': {'ucum_code': 'a'}} })
    method: Optional[EnumSampleCollectionMethod] = Field(default=None, title="Biospecimen Collection Method", description="""The approach used to collect the biospecimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    site: Optional[EnumSite] = Field(default=None, title="Biospecimen Collection Site", description="""The location of the specimen collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    spatial_qualifier: Optional[EnumSpatialQualifiers] = Field(default=None, title="Spatial Qualifier", description="""Qualifier that further refine the specific location of biospecimen collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    laterality: Optional[EnumLaterality] = Field(default=None, title="Location Laterality", description="""Laterality that further refine the specific location of biospecimen collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    encounter_id: Optional[str] = Field(default=None, title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Aliquot(Record):
    """
    A specific tube or amount of a biospecimen associated with a Sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'aliquot_id': {'identifier': True,
                                       'name': 'aliquot_id',
                                       'range': 'string',
                                       'required': True}},
         'title': 'Aliquot'})

    aliquot_id: str = Field(default=..., title="Aliquot ID", description="""Unique identifier for an Aliquot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    sample_id: Optional[str] = Field(default=None, title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'FileAdmin', 'FileAssay']} })
    availablity_status: Optional[EnumAvailabilityStatus] = Field(default=None, title="Sample Availability", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_unit: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    concentration_number: Optional[float] = Field(default=None, title="Concentration", description="""What is the concentration of the analyte in the Aliquot?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    concentration_unit: Optional[str] = Field(default=None, title="Concentration Units", description="""Units associated with the concentration of the analyte in the Aliquot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Encounter(Record):
    """
    An event at which data was collected about a participant, an intervention was made, or information about a participant was recorded.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'encounter_id': {'identifier': True,
                                         'name': 'encounter_id',
                                         'range': 'string',
                                         'required': True}},
         'title': 'Participant Encounter'})

    encounter_id: str = Field(default=..., title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    subject_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    encounter_definition_id: Optional[str] = Field(default=None, title="Encounter Definition ID", description="""Unique identifier for this Encounter Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Encounter', 'EncounterDefinition']} })
    age_at_event: Optional[int] = Field(default=None, title="Age at event", description="""The age in days of the Subject at the time point which the assertion describes, eg, age of onset or when a measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'Encounter'], 'unit': {'ucum_code': 'd'}} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class EncounterDefinition(Record):
    """
    A definition of an encounter type in this study, ie, an event at which data was collected about a participant, an intervention was made, or information about a participant was recorded. This may be something planned by a study or a type of data collection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'activity_definition_id': {'multivalued': True,
                                                   'name': 'activity_definition_id'},
                        'encounter_definition_id': {'identifier': True,
                                                    'name': 'encounter_definition_id',
                                                    'range': 'string',
                                                    'required': True}},
         'title': 'Encounter Definition'})

    encounter_definition_id: str = Field(default=..., title="Encounter Definition ID", description="""Unique identifier for this Encounter Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Encounter', 'EncounterDefinition']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    activity_definition_id: Optional[list[str]] = Field(default=[], title="Activity Definition ID", description="""Unique identifier for this Activity Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class ActivityDefinition(Record):
    """
    A definition of an activity in this study, eg, a biospecimen collection, intervention, survey, or assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'activity_definition_id': {'identifier': True,
                                                   'name': 'activity_definition_id',
                                                   'range': 'string',
                                                   'required': True}},
         'title': 'Activity Definition'})

    activity_definition_id: str = Field(default=..., title="Activity Definition ID", description="""Unique identifier for this Activity Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class File(Record):
    """
    Required information for portal use.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'data_category': {'name': 'data_category', 'required': True},
                        'file_id': {'identifier': True,
                                    'name': 'file_id',
                                    'range': 'string',
                                    'required': True},
                        'sample_id': {'multivalued': True,
                                      'name': 'sample_id',
                                      'required': True},
                        'study_id': {'name': 'study_id', 'required': True},
                        'subject_id': {'multivalued': True,
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'File'})

    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'StudyMetadata', 'File', 'FileAdmin']} })
    file_id: str = Field(default=..., title="File ID", description="""Unique identifier for this File.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Dataset', 'FileAdmin', 'FileAssay']} })
    subject_id: list[str] = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    sample_id: list[str] = Field(default=..., title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'FileAdmin', 'FileAssay']} })
    s3_file_path: str = Field(default=..., title="S3 File Path", description="""The full s3 url of a file's location in aws""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    filename: str = Field(default=..., title="Filename", description="""The name of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    size: int = Field(default=..., title="File Size", description="""Size of the file, in Bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin', 'FileAssay'], 'unit': {'ucum_code': 'By'}} })
    format: EnumEDAMFormats = Field(default=..., title="File Format", description="""The format of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAssay']} })
    data_category: EnumDataCategory = Field(default=..., title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata', 'File', 'FileAssay']} })
    data_type: EnumEDAMDataTypes = Field(default=..., title="Data Type", description="""The type of data within this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAssay']} })
    staging_url: Optional[str] = Field(default=None, title="Staging Location", description="""URL for internal access to the data. May be temporary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    release_url: Optional[str] = Field(default=None, title="Release Location", description="""URL for controlled or open access to the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    drs_uri: Optional[str] = Field(default=None, title="DRS URI", description="""DRS location to access the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    hash: FileHash = Field(default=..., title="File Hash", description="""File hash information""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class FileHash(ConfiguredBaseModel):
    """
    Type and value of a file content hash.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'File Hash'})

    hash_type: EnumFileHashType = Field(default=..., title="File Hash Type", description="""The type of file hash, eg, md5""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileHash']} })
    hash_value: str = Field(default=..., title="File Hash Value", description="""The value of the file hash""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileHash']} })


class Dataset(ConfiguredBaseModel):
    """
    Set of files grouped together for release.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'dataset_id': {'identifier': True,
                                       'name': 'dataset_id',
                                       'range': 'string',
                                       'required': True},
                        'file_id': {'description': 'The list of files comprising this '
                                                   'dataset.',
                                    'multivalued': True,
                                    'name': 'file_id'}},
         'title': 'Dataset'})

    dataset_id: str = Field(default=..., title="Dataset ID", description="""Unique identifier for a Dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    do_id: Optional[str] = Field(default=None, title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    file_id: Optional[list[str]] = Field(default=[], title="File ID", description="""The list of files comprising this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Dataset', 'FileAdmin', 'FileAssay']} })
    publication: Optional[list[Publication]] = Field(default=[], title="Publication", description="""Publications associated with this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'Dataset']} })
    data_collection_start: Optional[str] = Field(default=None, title="Data Collection Start", description="""The date that data collection started. May include only a year.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_collection_end: Optional[str] = Field(default=None, title="Data Collection End", description="""The date that data collection started. May include only a year.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


class FileAdmin(ConfiguredBaseModel):
    """
    File unvierse; contains all information about a file that may be needed for operational work
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'file_id': {'identifier': True,
                                    'name': 'file_id',
                                    'required': True},
                        'study_id': {'name': 'study_id', 'required': True}}})

    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'StudyMetadata', 'File', 'FileAdmin']} })
    file_id: str = Field(default=..., title="File ID", description="""Unique identifier for this File.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Dataset', 'FileAdmin', 'FileAssay']} })
    subject_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    sample_id: Optional[str] = Field(default=None, title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'FileAdmin', 'FileAssay']} })
    s3_file_path: str = Field(default=..., title="S3 File Path", description="""The full s3 url of a file's location in aws""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    file_category: str = Field(default=..., title="File Category", description="""A high level classification of the file used for operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    size: int = Field(default=..., title="File Size", description="""Size of the file, in Bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin', 'FileAssay'], 'unit': {'ucum_code': 'By'}} })
    s3_key: str = Field(default=..., title="S3 Key", description="""The unique identifier for an object within a bucket""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    file_extension: str = Field(default=..., title="File Extension", description="""A 3-4 letter code at the end of a filename that identifies the file format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    data_transfer_id: Optional[str] = Field(default=None, title="Data Transfer ID", description="""A jira ticket number associated with a file transfer request to production bucket""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    aws_account_id: str = Field(default=..., title="AWS Account ID", description="""A 12-digit number that uniquely identifies a specific AWS account""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    account_name: str = Field(default=..., title="AWS Account Name", description="""A user-defined label used to define an AWS accoun.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    account_alias: str = Field(default=..., title="Account Alias", description="""A unique user-defined string that replaces the AWS Account ID in the IAM user sign-in URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    bucket_study_id: str = Field(default=..., title="Bucket Study ID", description="""The global study ID used to create the bucket""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    bucket: str = Field(default=..., title="Bucket", description="""Cloud storage container in AWS used to manage and store s3 objects""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    s3_created_at: datetime  = Field(default=..., title="S3 Created At", description="""Timestamp of when a file was uploaded to an s3 bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    s3_modified_at: datetime  = Field(default=..., title="S3 Modified At", description="""Timestamp of when a file was modified in an s3 bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    intelligent_tiering_access_tier: str = Field(default=..., title="Intelligent Tiering Access Tier", description="""Storage access tier assigned by AWS intelliegnt tiering, indicating the current access frequency classification of the object""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    is_delete_marker: bool = Field(default=..., title="Is Delete Marker", description="""A flag that notes whether a file has been deleted from s3""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    is_latest: bool = Field(default=..., title="Is Latest", description="""Specifies whether an object version is the most recent version of that object""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    storage_class: str = Field(default=..., title="Storage Class", description="""Storage tier of the object in AWS reflecting cost and access characteristics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    manifest_hash_value: Optional[str] = Field(default=None, title="Manifest Hash Value", description="""The provided hash value from external users to be validated against internal hash values""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    file_hash_validation_status: Optional[str] = Field(default=None, title="File Hash Validation Status", description="""Notes whether hashes have been generated and verified against manifest hash values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    file_type: str = Field(default=..., title="File Type", description="""An internal type or classification of the files based on its operational usuage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    encryption_status: str = Field(default=..., title="Encryption Status", description="""Indicates whether the object in AWS is encrypted and the type of encryption applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    is_multipart_uploaded: str = Field(default=..., title="Is Multipart Uploaded", description="""Indicates whether the object was uploaded using a multipart upload process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    object_lock_level_hold_status: str = Field(default=..., title="Object Lock Level Hold Status", description="""Whether a legal hold is applied to prevent deletion of the object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    object_lock_mode: str = Field(default=..., title="Object Lock Mode", description="""Retention mode applied to the object that restricts deletion or modification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    object_lock_retain_until_date: datetime  = Field(default=..., title="Object Lock Retain Until Date", description="""Specifies exact date and time when an object's Object Lock rentention period expires.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    replication_status: str = Field(default=..., title="Replication Status", description="""Status of the object's replication to another storage location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    version_id: str = Field(default=..., title="Version ID", description="""Identifier for a specific version of the object""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    staging_url: Optional[str] = Field(default=None, title="Staging Location", description="""URL for internal access to the data. May be temporary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    release_url: Optional[str] = Field(default=None, title="Release Location", description="""URL for controlled or open access to the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    hash: FileHash = Field(default=..., title="File Hash", description="""File hash information""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    access_type: EnumAccessType = Field(default=..., title="Access Type", description="""Notes wheter a file is controlled, open, or registered-tier access""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin', 'FileAssay']} })
    access_url: Optional[str] = Field(default=None, title="Access URL", description="""HTTPS endpoint for accessing a file via a specific data repository service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    drs_uri: Optional[str] = Field(default=None, title="DRS URI", description="""DRS location to access the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin']} })
    acl: str = Field(default=..., title="ACL", description="""The object access control list.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    is_released: bool = Field(default=..., title="Is Released", description="""A flag that notes whether a file has been released to the public""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    is_registered: bool = Field(default=..., title="Is Registered", description="""A flag that notes whether a file has been registered to a drs service""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    repository: Optional[EnumRepository] = Field(default=None, title="Repository", description="""The name of the drs service which files are registered to""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin']} })
    experimental_strategy: EnumExperimentalStrategy = Field(default=..., title="Experimental Strategy", description="""Method or assay used to generate the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin', 'FileAssay']} })


class FileAssay(ConfiguredBaseModel):
    """
    A file produced by or associated with an assay or data acquisition process including omics, imaging, actigraphy, and other experimental or observational data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'data_category': {'name': 'data_category', 'required': True},
                        'file_id': {'identifier': True,
                                    'name': 'file_id',
                                    'required': True},
                        'sample_id': {'multivalued': True,
                                      'name': 'sample_id',
                                      'required': True},
                        'subject_id': {'multivalued': True,
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'File Assay'})

    file_id: str = Field(default=..., title="File ID", description="""Unique identifier for this File.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Dataset', 'FileAdmin', 'FileAssay']} })
    subject_id: list[str] = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'FileAdmin',
                       'FileAssay']} })
    sample_id: list[str] = Field(default=..., title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'FileAdmin', 'FileAssay']} })
    data_category: EnumDataCategory = Field(default=..., title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata', 'File', 'FileAssay']} })
    experimental_strategy: EnumExperimentalStrategy = Field(default=..., title="Experimental Strategy", description="""Method or assay used to generate the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin', 'FileAssay']} })
    data_type: EnumEDAMDataTypes = Field(default=..., title="Data Type", description="""The type of data within this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAssay']} })
    format: EnumEDAMFormats = Field(default=..., title="File Format", description="""The format of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAssay']} })
    size: int = Field(default=..., title="File Size", description="""Size of the file, in Bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'FileAdmin', 'FileAssay'], 'unit': {'ucum_code': 'By'}} })
    access_type: EnumAccessType = Field(default=..., title="Access Type", description="""Notes wheter a file is controlled, open, or registered-tier access""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAdmin', 'FileAssay']} })
    assay_center: Optional[EnumAssayCenter] = Field(default=None, title="Assay Center", description="""The organization or center that generated the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAssay']} })
    platform: EnumPlatform = Field(default=..., title="Platform", description="""Instrument or platform family name""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAssay']} })
    workflow_name: Optional[str] = Field(default=None, title="Workflow Name", description="""Processing tool that produced the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAssay']} })
    workflow_version: Optional[str] = Field(default=None, title="Workflow Version", description="""Version of the process tool that produced the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileAssay']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Record.model_rebuild()
Study.model_rebuild()
StudyMetadata.model_rebuild()
VirtualBiorepository.model_rebuild()
DOI.model_rebuild()
Investigator.model_rebuild()
Publication.model_rebuild()
Subject.model_rebuild()
Demographics.model_rebuild()
SubjectAssertion.model_rebuild()
Concept.model_rebuild()
Sample.model_rebuild()
BiospecimenCollection.model_rebuild()
Aliquot.model_rebuild()
Encounter.model_rebuild()
EncounterDefinition.model_rebuild()
ActivityDefinition.model_rebuild()
File.model_rebuild()
FileHash.model_rebuild()
Dataset.model_rebuild()
FileAdmin.model_rebuild()
FileAssay.model_rebuild()
