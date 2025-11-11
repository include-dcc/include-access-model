# Auto generated from include_access_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-10T19:22:06
# Schema: include-access-model
#
# id: https://includedcc.org/include-access-model
# description: LinkML Schema for the internal INCLUDE DCC Access Model
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238/')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/')
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace('ig2_biospecimen_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/')
IG2DAC = CurieNamespace('ig2dac', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
IG2DAT = CurieNamespace('ig2dat', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/')
IG_DOB_METHOD = CurieNamespace('ig_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/')
IGCONDTYPE = CurieNamespace('igcondtype', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
INCLUDEDCC = CurieNamespace('includedcc', 'https://includedcc.org/include-access-model/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MESH = CurieNamespace('mesh', 'http://id.nlm.nih.gov/mesh/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SNOMED_CT = CurieNamespace('snomed_ct', 'http://snomed.info/id/')
DEFAULT_ = INCLUDEDCC


# Types

# Class references
class RecordId(extended_str):
    pass


class StudyId(RecordId):
    pass


class VirtualBiorepositoryId(RecordId):
    pass


class DOIId(RecordId):
    pass


class InvestigatorId(RecordId):
    pass


class PublicationId(RecordId):
    pass


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    One row / entity within the database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Record"]
    class_class_curie: ClassVar[str] = "includedcc:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Record

    id: Union[str, RecordId] = None
    uuid: str = None
    external_id: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordId):
            self.id = RecordId(self.id)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(Record):
    """
    Study Metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Study"]
    class_class_curie: ClassVar[str] = "includedcc:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Study

    id: Union[str, StudyId] = None
    uuid: str = None
    principal_investigator: Union[Union[str, InvestigatorId], list[Union[str, InvestigatorId]]] = None
    contact: Union[Union[str, InvestigatorId], list[Union[str, InvestigatorId]]] = None
    study_title: str = None
    study_code: str = None
    program: Union[Union[str, "EnumProgram"], list[Union[str, "EnumProgram"]]] = None
    study_description: str = None
    research_domain: Union[Union[str, "EnumResearchDomain"], list[Union[str, "EnumResearchDomain"]]] = None
    participant_lifespan_stage: Union[Union[str, "EnumParticipantLifespanStage"], list[Union[str, "EnumParticipantLifespanStage"]]] = None
    study_design: Union[Union[str, "EnumStudyDesign"], list[Union[str, "EnumStudyDesign"]]] = None
    clinical_data_source_type: Union[Union[str, "EnumClinicalDataSourceType"], list[Union[str, "EnumClinicalDataSourceType"]]] = None
    data_category: Union[Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]] = None
    expected_number_of_participants: int = None
    actual_number_of_participants: int = None
    parent_study: Optional[Union[str, StudyId]] = None
    funding_source: Optional[Union[str, list[str]]] = empty_list()
    study_short_name: Optional[str] = None
    vbr: Optional[Union[str, VirtualBiorepositoryId]] = None
    selection_criteria: Optional[str] = None
    website: Optional[Union[str, URI]] = None
    publication: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()
    acknowledgments: Optional[str] = None
    citation_statement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.principal_investigator):
            self.MissingRequiredField("principal_investigator")
        if not isinstance(self.principal_investigator, list):
            self.principal_investigator = [self.principal_investigator] if self.principal_investigator is not None else []
        self.principal_investigator = [v if isinstance(v, InvestigatorId) else InvestigatorId(v) for v in self.principal_investigator]

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, InvestigatorId) else InvestigatorId(v) for v in self.contact]

        if self._is_empty(self.study_title):
            self.MissingRequiredField("study_title")
        if not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self._is_empty(self.study_code):
            self.MissingRequiredField("study_code")
        if not isinstance(self.study_code, str):
            self.study_code = str(self.study_code)

        if self._is_empty(self.program):
            self.MissingRequiredField("program")
        if not isinstance(self.program, list):
            self.program = [self.program] if self.program is not None else []
        self.program = [v if isinstance(v, EnumProgram) else EnumProgram(v) for v in self.program]

        if self._is_empty(self.study_description):
            self.MissingRequiredField("study_description")
        if not isinstance(self.study_description, str):
            self.study_description = str(self.study_description)

        if self._is_empty(self.research_domain):
            self.MissingRequiredField("research_domain")
        if not isinstance(self.research_domain, list):
            self.research_domain = [self.research_domain] if self.research_domain is not None else []
        self.research_domain = [v if isinstance(v, EnumResearchDomain) else EnumResearchDomain(v) for v in self.research_domain]

        if self._is_empty(self.participant_lifespan_stage):
            self.MissingRequiredField("participant_lifespan_stage")
        if not isinstance(self.participant_lifespan_stage, list):
            self.participant_lifespan_stage = [self.participant_lifespan_stage] if self.participant_lifespan_stage is not None else []
        self.participant_lifespan_stage = [v if isinstance(v, EnumParticipantLifespanStage) else EnumParticipantLifespanStage(v) for v in self.participant_lifespan_stage]

        if self._is_empty(self.study_design):
            self.MissingRequiredField("study_design")
        if not isinstance(self.study_design, list):
            self.study_design = [self.study_design] if self.study_design is not None else []
        self.study_design = [v if isinstance(v, EnumStudyDesign) else EnumStudyDesign(v) for v in self.study_design]

        if self._is_empty(self.clinical_data_source_type):
            self.MissingRequiredField("clinical_data_source_type")
        if not isinstance(self.clinical_data_source_type, list):
            self.clinical_data_source_type = [self.clinical_data_source_type] if self.clinical_data_source_type is not None else []
        self.clinical_data_source_type = [v if isinstance(v, EnumClinicalDataSourceType) else EnumClinicalDataSourceType(v) for v in self.clinical_data_source_type]

        if self._is_empty(self.data_category):
            self.MissingRequiredField("data_category")
        if not isinstance(self.data_category, list):
            self.data_category = [self.data_category] if self.data_category is not None else []
        self.data_category = [v if isinstance(v, EnumDataCategory) else EnumDataCategory(v) for v in self.data_category]

        if self._is_empty(self.expected_number_of_participants):
            self.MissingRequiredField("expected_number_of_participants")
        if not isinstance(self.expected_number_of_participants, int):
            self.expected_number_of_participants = int(self.expected_number_of_participants)

        if self._is_empty(self.actual_number_of_participants):
            self.MissingRequiredField("actual_number_of_participants")
        if not isinstance(self.actual_number_of_participants, int):
            self.actual_number_of_participants = int(self.actual_number_of_participants)

        if self.parent_study is not None and not isinstance(self.parent_study, StudyId):
            self.parent_study = StudyId(self.parent_study)

        if not isinstance(self.funding_source, list):
            self.funding_source = [self.funding_source] if self.funding_source is not None else []
        self.funding_source = [v if isinstance(v, str) else str(v) for v in self.funding_source]

        if self.study_short_name is not None and not isinstance(self.study_short_name, str):
            self.study_short_name = str(self.study_short_name)

        if self.vbr is not None and not isinstance(self.vbr, VirtualBiorepositoryId):
            self.vbr = VirtualBiorepositoryId(self.vbr)

        if self.selection_criteria is not None and not isinstance(self.selection_criteria, str):
            self.selection_criteria = str(self.selection_criteria)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if not isinstance(self.publication, list):
            self.publication = [self.publication] if self.publication is not None else []
        self.publication = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publication]

        if self.acknowledgments is not None and not isinstance(self.acknowledgments, str):
            self.acknowledgments = str(self.acknowledgments)

        if self.citation_statement is not None and not isinstance(self.citation_statement, str):
            self.citation_statement = str(self.citation_statement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirtualBiorepository(Record):
    """
    An organization that can provide access to specimen for further analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["VirtualBiorepository"]
    class_class_curie: ClassVar[str] = "includedcc:VirtualBiorepository"
    class_name: ClassVar[str] = "VirtualBiorepository"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.VirtualBiorepository

    id: Union[str, VirtualBiorepositoryId] = None
    uuid: str = None
    contact: Union[Union[str, InvestigatorId], list[Union[str, InvestigatorId]]] = None
    name: Optional[str] = None
    institution: Optional[str] = None
    website: Optional[Union[str, URI]] = None
    vbr_readme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirtualBiorepositoryId):
            self.id = VirtualBiorepositoryId(self.id)

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, InvestigatorId) else InvestigatorId(v) for v in self.contact]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.vbr_readme is not None and not isinstance(self.vbr_readme, str):
            self.vbr_readme = str(self.vbr_readme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DOI(Record):
    """
    A DOI is a permanent reference with metadata about a digital object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["DOI"]
    class_class_curie: ClassVar[str] = "includedcc:DOI"
    class_name: ClassVar[str] = "DOI"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.DOI

    id: Union[str, DOIId] = None
    uuid: str = None
    doi: Optional[Union[str, DOIId]] = None
    bibliographic_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DOIId):
            self.id = DOIId(self.id)

        if self.doi is not None and not isinstance(self.doi, DOIId):
            self.doi = DOIId(self.doi)

        if self.bibliographic_reference is not None and not isinstance(self.bibliographic_reference, str):
            self.bibliographic_reference = str(self.bibliographic_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigator(Record):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Investigator"]
    class_class_curie: ClassVar[str] = "includedcc:Investigator"
    class_name: ClassVar[str] = "Investigator"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Investigator

    id: Union[str, InvestigatorId] = None
    uuid: str = None
    name: Optional[str] = None
    institution: Optional[str] = None
    invesitgator_title: Optional[str] = None
    email: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigatorId):
            self.id = InvestigatorId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.invesitgator_title is not None and not isinstance(self.invesitgator_title, str):
            self.invesitgator_title = str(self.invesitgator_title)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(Record):
    """
    Information about a specific publication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Publication"]
    class_class_curie: ClassVar[str] = "includedcc:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Publication

    id: Union[str, PublicationId] = None
    uuid: str = None
    bibliographic_reference: Optional[str] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.bibliographic_reference is not None and not isinstance(self.bibliographic_reference, str):
            self.bibliographic_reference = str(self.bibliographic_reference)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


# Enumerations
class EnumProgram(EnumDefinitionImpl):
    """
    Funding programs relevant to inform operations.
    """
    include = PermissibleValue(
        text="include",
        title="INCLUDE")
    kf = PermissibleValue(
        text="kf",
        title="KF")
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumProgram",
        description="Funding programs relevant to inform operations.",
    )

class EnumResearchDomain(EnumDefinitionImpl):
    """
    Domains of Research used to find studies.
    """
    behavior_and_behavior_mechanisms = PermissibleValue(
        text="behavior_and_behavior_mechanisms",
        title="Behavior and Behavior Mechanisms",
        meaning=MESH["D001520"])
    congenital_heart_defects = PermissibleValue(
        text="congenital_heart_defects",
        title="Congenital Heart Defects",
        meaning=MESH["D006330"])
    immune_system_diseases = PermissibleValue(
        text="immune_system_diseases",
        title="Immune System Diseases",
        meaning=MESH["D007154"])
    hematologic_diseases = PermissibleValue(
        text="hematologic_diseases",
        title="Hematologic Diseases",
        meaning=MESH["D006402"])
    neurodevelopment = PermissibleValue(
        text="neurodevelopment",
        title="Neurodevelopment",
        meaning=MESH["D065886"])
    sleep_wake_disorders = PermissibleValue(
        text="sleep_wake_disorders",
        title="Sleep Wake Disorders",
        meaning=MESH["D012893"])
    all_co_occurring_conditions = PermissibleValue(
        text="all_co_occurring_conditions",
        title="All Co-occurring Conditions",
        meaning=MESH["D013568"])
    physical_fitness = PermissibleValue(
        text="physical_fitness",
        title="Physical Fitness",
        meaning=MESH["D010809"])
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumResearchDomain",
        description="Domains of Research used to find studies.",
    )

class EnumParticipantLifespanStage(EnumDefinitionImpl):
    """
    Stages of life during which participants may be recruited.
    """
    fetal = PermissibleValue(
        text="fetal",
        title="Fetal",
        description="Before birth")
    neonatal = PermissibleValue(
        text="neonatal",
        title="Neonatal",
        description="0-28 days old")
    pediatric = PermissibleValue(
        text="pediatric",
        title="Pediatric",
        description="Birth-17 years old")
    adult = PermissibleValue(
        text="adult",
        title="Adult",
        description="18+ years old")

    _defn = EnumDefinition(
        name="EnumParticipantLifespanStage",
        description="Stages of life during which participants may be recruited.",
    )

class EnumStudyDesign(EnumDefinitionImpl):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    case_control = PermissibleValue(
        text="case_control",
        title="Case-Control")
    case_set = PermissibleValue(
        text="case_set",
        title="Case Set")
    control_set = PermissibleValue(
        text="control_set",
        title="Control Set")
    clinical_trial = PermissibleValue(
        text="clinical_trial",
        title="Clinical Trial")
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        title="Cross-Sectional")
    family_twins_trios = PermissibleValue(
        text="family_twins_trios",
        title="Family/Twins/Trios")
    interventional = PermissibleValue(
        text="interventional",
        title="Interventional")
    longitudinal = PermissibleValue(
        text="longitudinal",
        title="Longitudinal")
    trial_readiness_study = PermissibleValue(
        text="trial_readiness_study",
        title="Trial Readiness Study")
    tumor_vs_matched_normal = PermissibleValue(
        text="tumor_vs_matched_normal",
        title="Tumor vs Matched Normal")

    _defn = EnumDefinition(
        name="EnumStudyDesign",
        description="Approaches for collecting data, investigating interventions, and/or analyzing data.",
    )

class EnumClinicalDataSourceType(EnumDefinitionImpl):
    """
    Approaches to ascertain clinical information about a participant.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained directly from medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown")

    _defn = EnumDefinition(
        name="EnumClinicalDataSourceType",
        description="Approaches to ascertain clinical information about a participant.",
    )

class EnumDataCategory(EnumDefinitionImpl):
    """
    Categories of data which may be collected about participants.
    """
    unharmonized_demographic_clinical_data = PermissibleValue(
        text="unharmonized_demographic_clinical_data",
        title="Unharmonized Demographic/Clinical Data")
    harmonized_demographic_clinical_data = PermissibleValue(
        text="harmonized_demographic_clinical_data",
        title="Harmonized Demographic/Clinical Data")
    genomics = PermissibleValue(
        text="genomics",
        title="Genomics")
    transcriptomics = PermissibleValue(
        text="transcriptomics",
        title="Transcriptomics")
    epigenomics = PermissibleValue(
        text="epigenomics",
        title="Epigenomics")
    proteomics = PermissibleValue(
        text="proteomics",
        title="Proteomics")
    metabolomics = PermissibleValue(
        text="metabolomics",
        title="Metabolomics")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral",
        title="Cognitive/Behavioral")
    immune_profiling = PermissibleValue(
        text="immune_profiling",
        title="Immune Profiling")
    imaging = PermissibleValue(
        text="imaging",
        title="Imaging")
    microbiome = PermissibleValue(
        text="microbiome",
        title="Microbiome")
    fitness = PermissibleValue(
        text="fitness",
        title="Fitness")
    physical_activity = PermissibleValue(
        text="physical_activity",
        title="Physical Activity")
    other = PermissibleValue(
        text="other",
        title="Other")
    sleep_study = PermissibleValue(
        text="sleep_study",
        title="Sleep Study")

    _defn = EnumDefinition(
        name="EnumDataCategory",
        description="Categories of data which may be collected about participants.",
    )

# Slots
class slots:
    pass

slots.uuid = Slot(uri=INCLUDEDCC.uuid, name="uuid", curie=INCLUDEDCC.curie('uuid'),
                   model_uri=INCLUDEDCC.uuid, domain=None, range=str)

slots.id = Slot(uri=INCLUDEDCC.id, name="id", curie=INCLUDEDCC.curie('id'),
                   model_uri=INCLUDEDCC.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=INCLUDEDCC.external_id, name="external_id", curie=INCLUDEDCC.curie('external_id'),
                   model_uri=INCLUDEDCC.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.parent_study = Slot(uri=INCLUDEDCC.parent_study, name="parent_study", curie=INCLUDEDCC.curie('parent_study'),
                   model_uri=INCLUDEDCC.parent_study, domain=None, range=Optional[Union[str, StudyId]])

slots.funding_source = Slot(uri=INCLUDEDCC.funding_source, name="funding_source", curie=INCLUDEDCC.curie('funding_source'),
                   model_uri=INCLUDEDCC.funding_source, domain=None, range=Optional[Union[str, list[str]]])

slots.principal_investigator = Slot(uri=INCLUDEDCC.principal_investigator, name="principal_investigator", curie=INCLUDEDCC.curie('principal_investigator'),
                   model_uri=INCLUDEDCC.principal_investigator, domain=None, range=Union[Union[str, InvestigatorId], list[Union[str, InvestigatorId]]])

slots.study_title = Slot(uri=INCLUDEDCC.study_title, name="study_title", curie=INCLUDEDCC.curie('study_title'),
                   model_uri=INCLUDEDCC.study_title, domain=None, range=str)

slots.study_code = Slot(uri=INCLUDEDCC.study_code, name="study_code", curie=INCLUDEDCC.curie('study_code'),
                   model_uri=INCLUDEDCC.study_code, domain=None, range=str)

slots.study_short_name = Slot(uri=INCLUDEDCC.study_short_name, name="study_short_name", curie=INCLUDEDCC.curie('study_short_name'),
                   model_uri=INCLUDEDCC.study_short_name, domain=None, range=Optional[str])

slots.invesitgator_title = Slot(uri=INCLUDEDCC.invesitgator_title, name="invesitgator_title", curie=INCLUDEDCC.curie('invesitgator_title'),
                   model_uri=INCLUDEDCC.invesitgator_title, domain=None, range=Optional[str])

slots.name = Slot(uri=INCLUDEDCC.name, name="name", curie=INCLUDEDCC.curie('name'),
                   model_uri=INCLUDEDCC.name, domain=None, range=Optional[str])

slots.email = Slot(uri=INCLUDEDCC.email, name="email", curie=INCLUDEDCC.curie('email'),
                   model_uri=INCLUDEDCC.email, domain=None, range=Optional[str])

slots.institution = Slot(uri=INCLUDEDCC.institution, name="institution", curie=INCLUDEDCC.curie('institution'),
                   model_uri=INCLUDEDCC.institution, domain=None, range=Optional[str])

slots.program = Slot(uri=INCLUDEDCC.program, name="program", curie=INCLUDEDCC.curie('program'),
                   model_uri=INCLUDEDCC.program, domain=None, range=Union[Union[str, "EnumProgram"], list[Union[str, "EnumProgram"]]])

slots.study_description = Slot(uri=INCLUDEDCC.study_description, name="study_description", curie=INCLUDEDCC.curie('study_description'),
                   model_uri=INCLUDEDCC.study_description, domain=None, range=str)

slots.website = Slot(uri=INCLUDEDCC.website, name="website", curie=INCLUDEDCC.curie('website'),
                   model_uri=INCLUDEDCC.website, domain=None, range=Optional[Union[str, URI]])

slots.contact = Slot(uri=INCLUDEDCC.contact, name="contact", curie=INCLUDEDCC.curie('contact'),
                   model_uri=INCLUDEDCC.contact, domain=None, range=Union[Union[str, InvestigatorId], list[Union[str, InvestigatorId]]])

slots.vbr = Slot(uri=INCLUDEDCC.vbr, name="vbr", curie=INCLUDEDCC.curie('vbr'),
                   model_uri=INCLUDEDCC.vbr, domain=None, range=Optional[Union[str, VirtualBiorepositoryId]])

slots.vbr_readme = Slot(uri=INCLUDEDCC.vbr_readme, name="vbr_readme", curie=INCLUDEDCC.curie('vbr_readme'),
                   model_uri=INCLUDEDCC.vbr_readme, domain=None, range=Optional[str])

slots.research_domain = Slot(uri=INCLUDEDCC.research_domain, name="research_domain", curie=INCLUDEDCC.curie('research_domain'),
                   model_uri=INCLUDEDCC.research_domain, domain=None, range=Union[Union[str, "EnumResearchDomain"], list[Union[str, "EnumResearchDomain"]]])

slots.participant_lifespan_stage = Slot(uri=INCLUDEDCC.participant_lifespan_stage, name="participant_lifespan_stage", curie=INCLUDEDCC.curie('participant_lifespan_stage'),
                   model_uri=INCLUDEDCC.participant_lifespan_stage, domain=None, range=Union[Union[str, "EnumParticipantLifespanStage"], list[Union[str, "EnumParticipantLifespanStage"]]])

slots.selection_criteria = Slot(uri=INCLUDEDCC.selection_criteria, name="selection_criteria", curie=INCLUDEDCC.curie('selection_criteria'),
                   model_uri=INCLUDEDCC.selection_criteria, domain=None, range=Optional[str])

slots.study_design = Slot(uri=INCLUDEDCC.study_design, name="study_design", curie=INCLUDEDCC.curie('study_design'),
                   model_uri=INCLUDEDCC.study_design, domain=None, range=Union[Union[str, "EnumStudyDesign"], list[Union[str, "EnumStudyDesign"]]])

slots.data_category = Slot(uri=INCLUDEDCC.data_category, name="data_category", curie=INCLUDEDCC.curie('data_category'),
                   model_uri=INCLUDEDCC.data_category, domain=None, range=Union[Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]])

slots.clinical_data_source_type = Slot(uri=INCLUDEDCC.clinical_data_source_type, name="clinical_data_source_type", curie=INCLUDEDCC.curie('clinical_data_source_type'),
                   model_uri=INCLUDEDCC.clinical_data_source_type, domain=None, range=Union[Union[str, "EnumClinicalDataSourceType"], list[Union[str, "EnumClinicalDataSourceType"]]])

slots.publication = Slot(uri=INCLUDEDCC.publication, name="publication", curie=INCLUDEDCC.curie('publication'),
                   model_uri=INCLUDEDCC.publication, domain=None, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.expected_number_of_participants = Slot(uri=INCLUDEDCC.expected_number_of_participants, name="expected_number_of_participants", curie=INCLUDEDCC.curie('expected_number_of_participants'),
                   model_uri=INCLUDEDCC.expected_number_of_participants, domain=None, range=int)

slots.actual_number_of_participants = Slot(uri=INCLUDEDCC.actual_number_of_participants, name="actual_number_of_participants", curie=INCLUDEDCC.curie('actual_number_of_participants'),
                   model_uri=INCLUDEDCC.actual_number_of_participants, domain=None, range=int)

slots.acknowledgments = Slot(uri=INCLUDEDCC.acknowledgments, name="acknowledgments", curie=INCLUDEDCC.curie('acknowledgments'),
                   model_uri=INCLUDEDCC.acknowledgments, domain=None, range=Optional[str])

slots.citation_statement = Slot(uri=INCLUDEDCC.citation_statement, name="citation_statement", curie=INCLUDEDCC.curie('citation_statement'),
                   model_uri=INCLUDEDCC.citation_statement, domain=None, range=Optional[str])

slots.bibliographic_reference = Slot(uri=INCLUDEDCC.bibliographic_reference, name="bibliographic_reference", curie=INCLUDEDCC.curie('bibliographic_reference'),
                   model_uri=INCLUDEDCC.bibliographic_reference, domain=None, range=Optional[str])

slots.doi = Slot(uri=INCLUDEDCC.doi, name="doi", curie=INCLUDEDCC.curie('doi'),
                   model_uri=INCLUDEDCC.doi, domain=None, range=Optional[Union[str, DOIId]])
