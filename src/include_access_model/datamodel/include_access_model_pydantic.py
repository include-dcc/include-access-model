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
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ncit_'},
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
    Types of entities
    """
    participant = "participant"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    non_participant = "non_participant"
    """
    An individual associated with a study who was not explictly consented, eg, the subject | of a reported family history.
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
    D21 = "d21"
    """
    Disomy 21 (euploid)
    """
    T21 = "t21"
    """
    Trisomy 21 (Down syndrome)
    """


class EnumSex(str, Enum):
    Female = "female"
    Male = "male"
    Other = "other"
    Unknown = "unknown"


class EnumRace(str, Enum):
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
    Hispanic_or_Latino = "hispanic_or_latino"
    Not_Hispanic_or_Latino = "not_hispanic_or_latino"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"


class EnumVitalStatus(str, Enum):
    Dead = "dead"
    Alive = "alive"


class EnumNull(str, Enum):
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
                                     'required': True}},
         'title': 'Study'})

    study_id: str = Field(default=..., title="Study ID", description="""INLCUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    parent_study: Optional[str] = Field(default=None, title="Parent Study", description="""The parent study for this study, if it is a nested study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    funding_source: Optional[list[str]] = Field(default=[], title="Funding Source", description="""The funding source(s) of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: list[Investigator] = Field(default=..., title="Principal Investigator", description="""The Principal Investigator(s) responsible for the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    contact: list[Investigator] = Field(default=..., title="Contact Person", description="""The individual to contact with questions about this record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository']} })
    study_title: str = Field(default=..., description="""Full Study Title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_code: str = Field(default=..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_short_name: Optional[str] = Field(default=None, title="Study Code", description="""Short name for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    program: list[EnumProgram] = Field(default=..., title="Program", description="""Funding source(s) for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_description: str = Field(default=..., title="Study Description", description="""Brief description of the study (2-4 sentences)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    vbr: Optional[VirtualBiorepository] = Field(default=None, title="Virtual Biorepository", description="""Information about the study's Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    research_domain: list[EnumResearchDomain] = Field(default=..., description="""Main research domain(s) of the study, other than Down syndrome""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    participant_lifespan_stage: list[EnumParticipantLifespanStage] = Field(default=..., title="Participant Lifespan Stage", description="""Focus age group(s) of the study population""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    selection_criteria: Optional[str] = Field(default=None, title="Selection Criteria", description="""Brief description of inclusion and/or exclusion criteria for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_design: list[EnumStudyDesign] = Field(default=..., title="Study Design", description="""Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    clinical_data_source_type: list[EnumClinicalDataSourceType] = Field(default=..., title="Clinical Data Source Type", description="""Source(s) of data collected from study participants""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    data_category: list[EnumDataCategory] = Field(default=..., title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website for the Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository', 'Publication']} })
    publication: Optional[list[Publication]] = Field(default=[], title="Publication", description="""Publications associated with this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    expected_number_of_participants: int = Field(default=..., title="Expected Number of Participants", description="""Total expected number of participants to be recruited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    actual_number_of_participants: int = Field(default=..., title="Actual Number of Participants", description="""Total participants included at this time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    acknowledgments: Optional[str] = Field(default=None, title="Acknowledgments", description="""Funding statement and acknowledgments for this study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    citation_statement: Optional[str] = Field(default=None, title="Citation Statement", description="""Statement that secondary data users should use to acknowledge use of this study or dataset. E.g., \"The results analyzed and <published or shown> here are based in whole or in part upon data generated by the INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE) Project <insert accession number(s) and/or study DOI(s)>, and were accessed from the INCLUDE Data Hub and <insert other database(s)>.\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    doi: Optional[str] = Field(default=None, title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class VirtualBiorepository(Record):
    """
    An organization that can provide access to specimen for further analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Virtual BioRepository (VBR)'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
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
         'slot_usage': {'doi': {'identifier': True, 'name': 'doi', 'required': True}},
         'title': 'Digital Object Identifier (DOI)'})

    doi: str = Field(default=..., title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI']} })
    bibliographic_reference: Optional[str] = Field(default=None, title="Bibiliographic Reference", description="""Text use to reference this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DOI', 'Publication']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Investigator(Record):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'title': 'Investigator'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""Name of the institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    invesitgator_title: Optional[str] = Field(default=None, title="Investigator Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigator']} })
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
    This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/include-access-model',
         'slot_usage': {'subject_id': {'identifier': True,
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'Subject'})

    subject_id: str = Field(default=..., title="Study ID", description="""INLCUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject', 'Demographics']} })
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

    subject_id: str = Field(default=..., title="Study ID", description="""INLCUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject', 'Demographics']} })
    sex: EnumSex = Field(default=..., title="Sex", description="""Sex of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    race: list[EnumRace] = Field(default=..., title="Race", description="""Race of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    ethnicity: EnumEthnicity = Field(default=..., title="Ethnicity", description="""Ethnicity of Participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    down_syndrome_status: EnumDownSyndromeStatus = Field(default=..., title="Down Syndrome Status", description="""Down Syndrome status of participant""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    age_at_last_vital_status: Optional[int] = Field(default=None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    vital_status: Optional[EnumVitalStatus] = Field(default=None, title="Vital Status", description="""Whether participant is alive or dead""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    age_at_first_engagement: Optional[int] = Field(default=None, title="Age at First Participant Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Record.model_rebuild()
Study.model_rebuild()
VirtualBiorepository.model_rebuild()
DOI.model_rebuild()
Investigator.model_rebuild()
Publication.model_rebuild()
Subject.model_rebuild()
Demographics.model_rebuild()
