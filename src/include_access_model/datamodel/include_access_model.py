# Auto generated from include_access_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-10T14:06:57
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

from linkml_runtime.linkml_model.types import Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
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
class StudyStudyId(extended_str):
    pass


class StudyMetadataStudyId(StudyStudyId):
    pass


class VirtualBiorepositoryVbrId(extended_str):
    pass


class DOIDoId(extended_str):
    pass


class SubjectSubjectId(extended_str):
    pass


class DemographicsSubjectId(SubjectSubjectId):
    pass


class SubjectAssertionAssertionId(extended_str):
    pass


class ConceptConceptCurie(URIorCURIE):
    pass


class SampleSampleId(extended_str):
    pass


class BiospecimenCollectionBiospecimenCollectionId(extended_str):
    pass


class AliquotAliquotId(extended_str):
    pass


class EncounterEncounterId(extended_str):
    pass


class EncounterDefinitionEncounterDefinitionId(extended_str):
    pass


class ActivityDefinitionActivityDefinitionId(extended_str):
    pass


class FileFileId(extended_str):
    pass


class DatasetDatasetId(extended_str):
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

    external_id: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
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

    study_id: Union[str, StudyStudyId] = None
    study_title: str = None
    study_code: str = None
    program: Union[Union[str, "EnumProgram"], list[Union[str, "EnumProgram"]]] = None
    principal_investigator: Union[Union[dict, "Investigator"], list[Union[dict, "Investigator"]]] = None
    contact: Union[Union[dict, "Investigator"], list[Union[dict, "Investigator"]]] = None
    study_description: str = None
    parent_study: Optional[Union[str, StudyStudyId]] = None
    study_short_name: Optional[str] = None
    funding_source: Optional[Union[str, list[str]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    publication: Optional[Union[Union[dict, "Publication"], list[Union[dict, "Publication"]]]] = empty_list()
    acknowledgments: Optional[str] = None
    citation_statement: Optional[str] = None
    do_id: Optional[Union[str, DOIDoId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyStudyId):
            self.study_id = StudyStudyId(self.study_id)

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

        if self._is_empty(self.principal_investigator):
            self.MissingRequiredField("principal_investigator")
        if not isinstance(self.principal_investigator, list):
            self.principal_investigator = [self.principal_investigator] if self.principal_investigator is not None else []
        self.principal_investigator = [v if isinstance(v, Investigator) else Investigator(**as_dict(v)) for v in self.principal_investigator]

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, Investigator) else Investigator(**as_dict(v)) for v in self.contact]

        if self._is_empty(self.study_description):
            self.MissingRequiredField("study_description")
        if not isinstance(self.study_description, str):
            self.study_description = str(self.study_description)

        if self.parent_study is not None and not isinstance(self.parent_study, StudyStudyId):
            self.parent_study = StudyStudyId(self.parent_study)

        if self.study_short_name is not None and not isinstance(self.study_short_name, str):
            self.study_short_name = str(self.study_short_name)

        if not isinstance(self.funding_source, list):
            self.funding_source = [self.funding_source] if self.funding_source is not None else []
        self.funding_source = [v if isinstance(v, str) else str(v) for v in self.funding_source]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if not isinstance(self.publication, list):
            self.publication = [self.publication] if self.publication is not None else []
        self.publication = [v if isinstance(v, Publication) else Publication(**as_dict(v)) for v in self.publication]

        if self.acknowledgments is not None and not isinstance(self.acknowledgments, str):
            self.acknowledgments = str(self.acknowledgments)

        if self.citation_statement is not None and not isinstance(self.citation_statement, str):
            self.citation_statement = str(self.citation_statement)

        if self.do_id is not None and not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyMetadata(Record):
    """
    Additional features about studies that may not apply to all studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["StudyMetadata"]
    class_class_curie: ClassVar[str] = "includedcc:StudyMetadata"
    class_name: ClassVar[str] = "StudyMetadata"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.StudyMetadata

    study_id: Union[str, StudyMetadataStudyId] = None
    participant_lifespan_stage: Union[Union[str, "EnumParticipantLifespanStage"], list[Union[str, "EnumParticipantLifespanStage"]]] = None
    study_design: Union[Union[str, "EnumStudyDesign"], list[Union[str, "EnumStudyDesign"]]] = None
    clinical_data_source_type: Union[Union[str, "EnumClinicalDataSourceType"], list[Union[str, "EnumClinicalDataSourceType"]]] = None
    data_category: Union[Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]] = None
    research_domain: Union[Union[str, "EnumResearchDomain"], list[Union[str, "EnumResearchDomain"]]] = None
    expected_number_of_participants: int = None
    actual_number_of_participants: int = None
    selection_criteria: Optional[str] = None
    vbr_id: Optional[Union[str, VirtualBiorepositoryVbrId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyMetadataStudyId):
            self.study_id = StudyMetadataStudyId(self.study_id)

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

        if self._is_empty(self.research_domain):
            self.MissingRequiredField("research_domain")
        if not isinstance(self.research_domain, list):
            self.research_domain = [self.research_domain] if self.research_domain is not None else []
        self.research_domain = [v if isinstance(v, EnumResearchDomain) else EnumResearchDomain(v) for v in self.research_domain]

        if self._is_empty(self.expected_number_of_participants):
            self.MissingRequiredField("expected_number_of_participants")
        if not isinstance(self.expected_number_of_participants, int):
            self.expected_number_of_participants = int(self.expected_number_of_participants)

        if self._is_empty(self.actual_number_of_participants):
            self.MissingRequiredField("actual_number_of_participants")
        if not isinstance(self.actual_number_of_participants, int):
            self.actual_number_of_participants = int(self.actual_number_of_participants)

        if self.selection_criteria is not None and not isinstance(self.selection_criteria, str):
            self.selection_criteria = str(self.selection_criteria)

        if self.vbr_id is not None and not isinstance(self.vbr_id, VirtualBiorepositoryVbrId):
            self.vbr_id = VirtualBiorepositoryVbrId(self.vbr_id)

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

    vbr_id: Union[str, VirtualBiorepositoryVbrId] = None
    contact: Union[Union[dict, "Investigator"], list[Union[dict, "Investigator"]]] = None
    name: Optional[str] = None
    institution: Optional[str] = None
    website: Optional[Union[str, URI]] = None
    vbr_readme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vbr_id):
            self.MissingRequiredField("vbr_id")
        if not isinstance(self.vbr_id, VirtualBiorepositoryVbrId):
            self.vbr_id = VirtualBiorepositoryVbrId(self.vbr_id)

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, Investigator) else Investigator(**as_dict(v)) for v in self.contact]

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

    do_id: Union[str, DOIDoId] = None
    bibliographic_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.do_id):
            self.MissingRequiredField("do_id")
        if not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

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

    name: Optional[str] = None
    institution: Optional[str] = None
    investigator_title: Optional[str] = None
    email: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.investigator_title is not None and not isinstance(self.investigator_title, str):
            self.investigator_title = str(self.investigator_title)

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

    bibliographic_reference: Optional[str] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bibliographic_reference is not None and not isinstance(self.bibliographic_reference, str):
            self.bibliographic_reference = str(self.bibliographic_reference)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(Record):
    """
    This entity is the subject about which data or references are recorded. This includes the idea of a human
    participant in a study, a cell line, an animal model, or any other similar entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Subject"]
    class_class_curie: ClassVar[str] = "includedcc:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Subject

    subject_id: Union[str, SubjectSubjectId] = None
    subject_type: Union[str, "EnumSubjectType"] = None
    organism_type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self._is_empty(self.subject_type):
            self.MissingRequiredField("subject_type")
        if not isinstance(self.subject_type, EnumSubjectType):
            self.subject_type = EnumSubjectType(self.subject_type)

        if self.organism_type is not None and not isinstance(self.organism_type, URIorCURIE):
            self.organism_type = URIorCURIE(self.organism_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Demographics(Record):
    """
    Basic participant demographics summary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Demographics"]
    class_class_curie: ClassVar[str] = "includedcc:Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Demographics

    subject_id: Union[str, DemographicsSubjectId] = None
    sex: Union[str, "EnumSex"] = None
    race: Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    down_syndrome_status: Union[str, "EnumDownSyndromeStatus"] = None
    age_at_last_vital_status: Optional[int] = None
    vital_status: Optional[Union[str, "EnumVitalStatus"]] = None
    age_at_first_engagement: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, DemographicsSubjectId):
            self.subject_id = DemographicsSubjectId(self.subject_id)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, list):
            self.race = [self.race] if self.race is not None else []
        self.race = [v if isinstance(v, EnumRace) else EnumRace(v) for v in self.race]

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self._is_empty(self.down_syndrome_status):
            self.MissingRequiredField("down_syndrome_status")
        if not isinstance(self.down_syndrome_status, EnumDownSyndromeStatus):
            self.down_syndrome_status = EnumDownSyndromeStatus(self.down_syndrome_status)

        if self.age_at_last_vital_status is not None and not isinstance(self.age_at_last_vital_status, int):
            self.age_at_last_vital_status = int(self.age_at_last_vital_status)

        if self.vital_status is not None and not isinstance(self.vital_status, EnumVitalStatus):
            self.vital_status = EnumVitalStatus(self.vital_status)

        if self.age_at_first_engagement is not None and not isinstance(self.age_at_first_engagement, int):
            self.age_at_first_engagement = int(self.age_at_first_engagement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectAssertion(Record):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["SubjectAssertion"]
    class_class_curie: ClassVar[str] = "includedcc:SubjectAssertion"
    class_name: ClassVar[str] = "SubjectAssertion"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.SubjectAssertion

    assertion_id: Union[str, SubjectAssertionAssertionId] = None
    subject_id: Optional[Union[str, SubjectSubjectId]] = None
    encounter_id: Optional[Union[str, EncounterEncounterId]] = None
    assertion_provenance: Optional[Union[str, "EnumAssertionProvenance"]] = None
    age_at_assertion: Optional[int] = None
    age_at_event: Optional[int] = None
    age_at_resolution: Optional[int] = None
    concept: Optional[Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]] = empty_list()
    concept_source: Optional[str] = None
    value_concept: Optional[Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]] = empty_list()
    value_number: Optional[float] = None
    value_source: Optional[str] = None
    value_unit: Optional[Union[str, ConceptConceptCurie]] = None
    value_unit_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assertion_id):
            self.MissingRequiredField("assertion_id")
        if not isinstance(self.assertion_id, SubjectAssertionAssertionId):
            self.assertion_id = SubjectAssertionAssertionId(self.assertion_id)

        if self.subject_id is not None and not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self.encounter_id is not None and not isinstance(self.encounter_id, EncounterEncounterId):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        if self.assertion_provenance is not None and not isinstance(self.assertion_provenance, EnumAssertionProvenance):
            self.assertion_provenance = EnumAssertionProvenance(self.assertion_provenance)

        if self.age_at_assertion is not None and not isinstance(self.age_at_assertion, int):
            self.age_at_assertion = int(self.age_at_assertion)

        if self.age_at_event is not None and not isinstance(self.age_at_event, int):
            self.age_at_event = int(self.age_at_event)

        if self.age_at_resolution is not None and not isinstance(self.age_at_resolution, int):
            self.age_at_resolution = int(self.age_at_resolution)

        if not isinstance(self.concept, list):
            self.concept = [self.concept] if self.concept is not None else []
        self.concept = [v if isinstance(v, ConceptConceptCurie) else ConceptConceptCurie(v) for v in self.concept]

        if self.concept_source is not None and not isinstance(self.concept_source, str):
            self.concept_source = str(self.concept_source)

        if not isinstance(self.value_concept, list):
            self.value_concept = [self.value_concept] if self.value_concept is not None else []
        self.value_concept = [v if isinstance(v, ConceptConceptCurie) else ConceptConceptCurie(v) for v in self.value_concept]

        if self.value_number is not None and not isinstance(self.value_number, float):
            self.value_number = float(self.value_number)

        if self.value_source is not None and not isinstance(self.value_source, str):
            self.value_source = str(self.value_source)

        if self.value_unit is not None and not isinstance(self.value_unit, ConceptConceptCurie):
            self.value_unit = ConceptConceptCurie(self.value_unit)

        if self.value_unit_source is not None and not isinstance(self.value_unit_source, str):
            self.value_unit_source = str(self.value_unit_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    A standardized concept with display information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Concept"]
    class_class_curie: ClassVar[str] = "includedcc:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Concept

    concept_curie: Union[str, ConceptConceptCurie] = None
    display: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_curie):
            self.MissingRequiredField("concept_curie")
        if not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(Record):
    """
    A functionally equivalent specimen taken from a participant or processed from such a sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Sample"]
    class_class_curie: ClassVar[str] = "includedcc:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Sample

    sample_id: Union[str, SampleSampleId] = None
    sample_type: Union[str, URIorCURIE] = None
    biospecimen_collection_id: Optional[Union[str, BiospecimenCollectionBiospecimenCollectionId]] = None
    parent_sample_id: Optional[Union[str, SampleSampleId]] = None
    processing: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    availablity_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    storage_method: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    quantity_number: Optional[float] = None
    quantity_unit: Optional[Union[str, ConceptConceptCurie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, URIorCURIE):
            self.sample_type = URIorCURIE(self.sample_type)

        if self.biospecimen_collection_id is not None and not isinstance(self.biospecimen_collection_id, BiospecimenCollectionBiospecimenCollectionId):
            self.biospecimen_collection_id = BiospecimenCollectionBiospecimenCollectionId(self.biospecimen_collection_id)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, SampleSampleId):
            self.parent_sample_id = SampleSampleId(self.parent_sample_id)

        if not isinstance(self.processing, list):
            self.processing = [self.processing] if self.processing is not None else []
        self.processing = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.processing]

        if self.availablity_status is not None and not isinstance(self.availablity_status, EnumAvailabilityStatus):
            self.availablity_status = EnumAvailabilityStatus(self.availablity_status)

        if not isinstance(self.storage_method, list):
            self.storage_method = [self.storage_method] if self.storage_method is not None else []
        self.storage_method = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.storage_method]

        if self.quantity_number is not None and not isinstance(self.quantity_number, float):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_unit is not None and not isinstance(self.quantity_unit, ConceptConceptCurie):
            self.quantity_unit = ConceptConceptCurie(self.quantity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiospecimenCollection(Record):
    """
    A biospecimen collection event which yields one or more Samples.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["BiospecimenCollection"]
    class_class_curie: ClassVar[str] = "includedcc:BiospecimenCollection"
    class_name: ClassVar[str] = "BiospecimenCollection"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.BiospecimenCollection

    biospecimen_collection_id: Union[str, BiospecimenCollectionBiospecimenCollectionId] = None
    age_at_collection: Optional[float] = None
    method: Optional[Union[str, "EnumSampleCollectionMethod"]] = None
    site: Optional[Union[str, "EnumSite"]] = None
    spatial_qualifier: Optional[Union[str, "EnumSpatialQualifiers"]] = None
    laterality: Optional[Union[str, "EnumLaterality"]] = None
    encounter_id: Optional[Union[str, EncounterEncounterId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biospecimen_collection_id):
            self.MissingRequiredField("biospecimen_collection_id")
        if not isinstance(self.biospecimen_collection_id, BiospecimenCollectionBiospecimenCollectionId):
            self.biospecimen_collection_id = BiospecimenCollectionBiospecimenCollectionId(self.biospecimen_collection_id)

        if self.age_at_collection is not None and not isinstance(self.age_at_collection, float):
            self.age_at_collection = float(self.age_at_collection)

        if self.encounter_id is not None and not isinstance(self.encounter_id, EncounterEncounterId):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aliquot(Record):
    """
    A specific tube or amount of a biospecimen associated with a Sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Aliquot"]
    class_class_curie: ClassVar[str] = "includedcc:Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Aliquot

    aliquot_id: Union[str, AliquotAliquotId] = None
    sample_id: Optional[Union[str, SampleSampleId]] = None
    availablity_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    quantity_number: Optional[float] = None
    quantity_unit: Optional[Union[str, ConceptConceptCurie]] = None
    concentration_number: Optional[float] = None
    concentration_unit: Optional[Union[str, ConceptConceptCurie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aliquot_id):
            self.MissingRequiredField("aliquot_id")
        if not isinstance(self.aliquot_id, AliquotAliquotId):
            self.aliquot_id = AliquotAliquotId(self.aliquot_id)

        if self.sample_id is not None and not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self.availablity_status is not None and not isinstance(self.availablity_status, EnumAvailabilityStatus):
            self.availablity_status = EnumAvailabilityStatus(self.availablity_status)

        if self.quantity_number is not None and not isinstance(self.quantity_number, float):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_unit is not None and not isinstance(self.quantity_unit, ConceptConceptCurie):
            self.quantity_unit = ConceptConceptCurie(self.quantity_unit)

        if self.concentration_number is not None and not isinstance(self.concentration_number, float):
            self.concentration_number = float(self.concentration_number)

        if self.concentration_unit is not None and not isinstance(self.concentration_unit, ConceptConceptCurie):
            self.concentration_unit = ConceptConceptCurie(self.concentration_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Encounter(Record):
    """
    An event at which data was collected about a participant, an intervention was made, or information about a
    participant was recorded.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Encounter"]
    class_class_curie: ClassVar[str] = "includedcc:Encounter"
    class_name: ClassVar[str] = "Encounter"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Encounter

    encounter_id: Union[str, EncounterEncounterId] = None
    subject_id: Optional[Union[str, SubjectSubjectId]] = None
    encounter_definition_id: Optional[Union[str, EncounterDefinitionEncounterDefinitionId]] = None
    age_at_event: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.encounter_id):
            self.MissingRequiredField("encounter_id")
        if not isinstance(self.encounter_id, EncounterEncounterId):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        if self.subject_id is not None and not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self.encounter_definition_id is not None and not isinstance(self.encounter_definition_id, EncounterDefinitionEncounterDefinitionId):
            self.encounter_definition_id = EncounterDefinitionEncounterDefinitionId(self.encounter_definition_id)

        if self.age_at_event is not None and not isinstance(self.age_at_event, int):
            self.age_at_event = int(self.age_at_event)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EncounterDefinition(Record):
    """
    A definition of an encounter type in this study, ie, an event at which data was collected about a participant, an
    intervention was made, or information about a participant was recorded. This may be something planned by a study
    or a type of data collection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["EncounterDefinition"]
    class_class_curie: ClassVar[str] = "includedcc:EncounterDefinition"
    class_name: ClassVar[str] = "EncounterDefinition"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.EncounterDefinition

    encounter_definition_id: Union[str, EncounterDefinitionEncounterDefinitionId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    activity_definition_id: Optional[Union[Union[str, ActivityDefinitionActivityDefinitionId], list[Union[str, ActivityDefinitionActivityDefinitionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.encounter_definition_id):
            self.MissingRequiredField("encounter_definition_id")
        if not isinstance(self.encounter_definition_id, EncounterDefinitionEncounterDefinitionId):
            self.encounter_definition_id = EncounterDefinitionEncounterDefinitionId(self.encounter_definition_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.activity_definition_id, list):
            self.activity_definition_id = [self.activity_definition_id] if self.activity_definition_id is not None else []
        self.activity_definition_id = [v if isinstance(v, ActivityDefinitionActivityDefinitionId) else ActivityDefinitionActivityDefinitionId(v) for v in self.activity_definition_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityDefinition(Record):
    """
    A definition of an activity in this study, eg, a biospecimen collection, intervention, survey, or assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["ActivityDefinition"]
    class_class_curie: ClassVar[str] = "includedcc:ActivityDefinition"
    class_name: ClassVar[str] = "ActivityDefinition"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.ActivityDefinition

    activity_definition_id: Union[str, ActivityDefinitionActivityDefinitionId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity_definition_id):
            self.MissingRequiredField("activity_definition_id")
        if not isinstance(self.activity_definition_id, ActivityDefinitionActivityDefinitionId):
            self.activity_definition_id = ActivityDefinitionActivityDefinitionId(self.activity_definition_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(Record):
    """
    File
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["File"]
    class_class_curie: ClassVar[str] = "includedcc:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.File

    file_id: Union[str, FileFileId] = None
    subject_id: Optional[Union[Union[str, SubjectSubjectId], list[Union[str, SubjectSubjectId]]]] = empty_list()
    sample_id: Optional[Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]] = empty_list()
    filename: Optional[str] = None
    format: Optional[Union[str, "EnumEDAMFormats"]] = None
    data_category: Optional[Union[str, "EnumDataCategory"]] = None
    data_type: Optional[Union[str, "EnumEDAMDataTypes"]] = None
    size: Optional[int] = None
    staging_url: Optional[Union[str, URIorCURIE]] = None
    release_url: Optional[Union[str, URIorCURIE]] = None
    drs_uri: Optional[Union[str, URIorCURIE]] = None
    hash: Optional[Union[dict, "FileHash"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, FileFileId):
            self.file_id = FileFileId(self.file_id)

        if not isinstance(self.subject_id, list):
            self.subject_id = [self.subject_id] if self.subject_id is not None else []
        self.subject_id = [v if isinstance(v, SubjectSubjectId) else SubjectSubjectId(v) for v in self.subject_id]

        if not isinstance(self.sample_id, list):
            self.sample_id = [self.sample_id] if self.sample_id is not None else []
        self.sample_id = [v if isinstance(v, SampleSampleId) else SampleSampleId(v) for v in self.sample_id]

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.data_category is not None and not isinstance(self.data_category, EnumDataCategory):
            self.data_category = EnumDataCategory(self.data_category)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.staging_url is not None and not isinstance(self.staging_url, URIorCURIE):
            self.staging_url = URIorCURIE(self.staging_url)

        if self.release_url is not None and not isinstance(self.release_url, URIorCURIE):
            self.release_url = URIorCURIE(self.release_url)

        if self.drs_uri is not None and not isinstance(self.drs_uri, URIorCURIE):
            self.drs_uri = URIorCURIE(self.drs_uri)

        if self.hash is not None and not isinstance(self.hash, FileHash):
            self.hash = FileHash(**as_dict(self.hash))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileHash(YAMLRoot):
    """
    Type and value of a file content hash.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["FileHash"]
    class_class_curie: ClassVar[str] = "includedcc:FileHash"
    class_name: ClassVar[str] = "FileHash"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.FileHash

    hash_type: Optional[Union[str, "EnumFileHashType"]] = None
    hash_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hash_type is not None and not isinstance(self.hash_type, EnumFileHashType):
            self.hash_type = EnumFileHashType(self.hash_type)

        if self.hash_value is not None and not isinstance(self.hash_value, str):
            self.hash_value = str(self.hash_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    Set of files grouped together for release.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDEDCC["Dataset"]
    class_class_curie: ClassVar[str] = "includedcc:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = INCLUDEDCC.Dataset

    dataset_id: Union[str, DatasetDatasetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    do_id: Optional[Union[str, DOIDoId]] = None
    file_id: Optional[Union[Union[str, FileFileId], list[Union[str, FileFileId]]]] = empty_list()
    publication: Optional[Union[Union[dict, Publication], list[Union[dict, Publication]]]] = empty_list()
    data_collection_start: Optional[str] = None
    data_collection_end: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dataset_id):
            self.MissingRequiredField("dataset_id")
        if not isinstance(self.dataset_id, DatasetDatasetId):
            self.dataset_id = DatasetDatasetId(self.dataset_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.do_id is not None and not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

        if not isinstance(self.file_id, list):
            self.file_id = [self.file_id] if self.file_id is not None else []
        self.file_id = [v if isinstance(v, FileFileId) else FileFileId(v) for v in self.file_id]

        if not isinstance(self.publication, list):
            self.publication = [self.publication] if self.publication is not None else []
        self.publication = [v if isinstance(v, Publication) else Publication(**as_dict(v)) for v in self.publication]

        if self.data_collection_start is not None and not isinstance(self.data_collection_start, str):
            self.data_collection_start = str(self.data_collection_start)

        if self.data_collection_end is not None and not isinstance(self.data_collection_end, str):
            self.data_collection_end = str(self.data_collection_end)

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

class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of Subject entities
    """
    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.")
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.""")
    cell_line = PermissibleValue(
        text="cell_line",
        description="Cell Line")
    animal_model = PermissibleValue(
        text="animal_model",
        description="Animal model")
    group = PermissibleValue(
        text="group",
        description="A group of individuals or entities.")
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!")

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of Subject entities",
    )

class EnumDownSyndromeStatus(EnumDefinitionImpl):
    """
    Down syndrome / chromosome 21 status
    """
    d21 = PermissibleValue(
        text="d21",
        title="D21",
        description="Disomy 21 (euploid)",
        meaning=PATO["0001393"])
    t21 = PermissibleValue(
        text="t21",
        title="T21",
        description="Trisomy 21 (Down syndrome)",
        meaning=MONDO["0008608"])

    _defn = EnumDefinition(
        name="EnumDownSyndromeStatus",
        description="Down syndrome / chromosome 21 status",
    )

class EnumSex(EnumDefinitionImpl):
    """
    Subject Sex
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        meaning=NCIT["C16576"])
    male = PermissibleValue(
        text="male",
        title="Male",
        meaning=NCIT["C20197"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumSex",
        description="Subject Sex",
    )

class EnumRace(EnumDefinitionImpl):
    """
    Participant Race
    """
    american_indian_or_alaska_native = PermissibleValue(
        text="american_indian_or_alaska_native",
        title="American Indian or Alaska Native",
        meaning=NCIT["C41259"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=NCIT["C41260"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=NCIT["C16352"])
    more_than_one_race = PermissibleValue(
        text="more_than_one_race",
        title="More than one race",
        meaning=NCIT["C67109"])
    native_hawaiian_or_other_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_other_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=NCIT["C41219"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=NCIT["C41261"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])
    east_asian = PermissibleValue(
        text="east_asian",
        title="East Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C161419"])
    latin_american = PermissibleValue(
        text="latin_american",
        title="Latin American",
        description="UK only; do not use for US data",
        meaning=NCIT["C126531"])
    middle_eastern_or_north_african = PermissibleValue(
        text="middle_eastern_or_north_african",
        title="Middle Eastern or North African",
        description="UK only; do not use for US data",
        meaning=NCIT["C43866"])
    south_asian = PermissibleValue(
        text="south_asian",
        title="South Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C41263"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="Participant Race",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        title="Hispanic or Latino",
        meaning=NCIT["C17459"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        title="Not Hispanic or Latino",
        meaning=NCIT["C41222"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="Participant ethnicity, specific to Hispanic or Latino.",
    )

class EnumVitalStatus(EnumDefinitionImpl):
    """
    Descriptions of a Subject's vital status
    """
    dead = PermissibleValue(
        text="dead",
        title="Dead",
        meaning=NCIT["C28554"])
    alive = PermissibleValue(
        text="alive",
        title="Alive",
        meaning=NCIT["C37987"])

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Descriptions of a Subject's vital status",
    )

class EnumNull(EnumDefinitionImpl):
    """
    Base enumeration providing null options.
    """
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumNull",
        description="Base enumeration providing null options.",
    )

class EnumAssertionProvenance(EnumDefinitionImpl):
    """
    Possible data sources for assertions.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained from a medical record")
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

    _defn = EnumDefinition(
        name="EnumAssertionProvenance",
        description="Possible data sources for assertions.",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the biospecimen available for use?
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the biospecimen available for use?",
    )

class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.",
    )

class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is
    recommended.
    """
    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.""",
    )

class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """
    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="Any spatial/location qualifiers.",
    )

class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """
    _defn = EnumDefinition(
        name="EnumLaterality",
        description="Laterality information for the site",
    )

class EnumEDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMFormats",
        description="Data formats from the EDAM ontology.",
    )

class EnumEDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )

class EnumFileHashType(EnumDefinitionImpl):
    """
    Types of file hashes supported.
    """
    md5 = PermissibleValue(
        text="md5",
        title="MD5")
    etag = PermissibleValue(
        text="etag",
        title="ETag")
    sha1 = PermissibleValue(
        text="sha1",
        title="SHA-1")

    _defn = EnumDefinition(
        name="EnumFileHashType",
        description="Types of file hashes supported.",
    )

# Slots
class slots:
    pass

slots.study_id = Slot(uri=INCLUDEDCC.study_id, name="study_id", curie=INCLUDEDCC.curie('study_id'),
                   model_uri=INCLUDEDCC.study_id, domain=None, range=Optional[Union[str, StudyStudyId]])

slots.do_id = Slot(uri=INCLUDEDCC.do_id, name="do_id", curie=INCLUDEDCC.curie('do_id'),
                   model_uri=INCLUDEDCC.do_id, domain=None, range=Optional[Union[str, DOIDoId]])

slots.subject_id = Slot(uri=INCLUDEDCC.subject_id, name="subject_id", curie=INCLUDEDCC.curie('subject_id'),
                   model_uri=INCLUDEDCC.subject_id, domain=None, range=Optional[Union[str, SubjectSubjectId]])

slots.assertion_id = Slot(uri=INCLUDEDCC.assertion_id, name="assertion_id", curie=INCLUDEDCC.curie('assertion_id'),
                   model_uri=INCLUDEDCC.assertion_id, domain=None, range=Optional[Union[str, SubjectAssertionAssertionId]])

slots.external_id = Slot(uri=INCLUDEDCC.external_id, name="external_id", curie=INCLUDEDCC.curie('external_id'),
                   model_uri=INCLUDEDCC.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.parent_study = Slot(uri=INCLUDEDCC.parent_study, name="parent_study", curie=INCLUDEDCC.curie('parent_study'),
                   model_uri=INCLUDEDCC.parent_study, domain=None, range=Optional[Union[str, StudyStudyId]])

slots.funding_source = Slot(uri=INCLUDEDCC.funding_source, name="funding_source", curie=INCLUDEDCC.curie('funding_source'),
                   model_uri=INCLUDEDCC.funding_source, domain=None, range=Optional[Union[str, list[str]]])

slots.principal_investigator = Slot(uri=INCLUDEDCC.principal_investigator, name="principal_investigator", curie=INCLUDEDCC.curie('principal_investigator'),
                   model_uri=INCLUDEDCC.principal_investigator, domain=None, range=Union[Union[dict, Investigator], list[Union[dict, Investigator]]])

slots.study_title = Slot(uri=INCLUDEDCC.study_title, name="study_title", curie=INCLUDEDCC.curie('study_title'),
                   model_uri=INCLUDEDCC.study_title, domain=None, range=str)

slots.study_code = Slot(uri=INCLUDEDCC.study_code, name="study_code", curie=INCLUDEDCC.curie('study_code'),
                   model_uri=INCLUDEDCC.study_code, domain=None, range=str)

slots.study_short_name = Slot(uri=INCLUDEDCC.study_short_name, name="study_short_name", curie=INCLUDEDCC.curie('study_short_name'),
                   model_uri=INCLUDEDCC.study_short_name, domain=None, range=Optional[str])

slots.investigator_title = Slot(uri=INCLUDEDCC.investigator_title, name="investigator_title", curie=INCLUDEDCC.curie('investigator_title'),
                   model_uri=INCLUDEDCC.investigator_title, domain=None, range=Optional[str])

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
                   model_uri=INCLUDEDCC.contact, domain=None, range=Union[Union[dict, Investigator], list[Union[dict, Investigator]]])

slots.vbr_id = Slot(uri=INCLUDEDCC.vbr_id, name="vbr_id", curie=INCLUDEDCC.curie('vbr_id'),
                   model_uri=INCLUDEDCC.vbr_id, domain=None, range=Optional[Union[str, VirtualBiorepositoryVbrId]])

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
                   model_uri=INCLUDEDCC.data_category, domain=None, range=Optional[Union[str, "EnumDataCategory"]])

slots.clinical_data_source_type = Slot(uri=INCLUDEDCC.clinical_data_source_type, name="clinical_data_source_type", curie=INCLUDEDCC.curie('clinical_data_source_type'),
                   model_uri=INCLUDEDCC.clinical_data_source_type, domain=None, range=Union[Union[str, "EnumClinicalDataSourceType"], list[Union[str, "EnumClinicalDataSourceType"]]])

slots.publication = Slot(uri=INCLUDEDCC.publication, name="publication", curie=INCLUDEDCC.curie('publication'),
                   model_uri=INCLUDEDCC.publication, domain=None, range=Optional[Union[Union[dict, Publication], list[Union[dict, Publication]]]])

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

slots.organism_type = Slot(uri=INCLUDEDCC.organism_type, name="organism_type", curie=INCLUDEDCC.curie('organism_type'),
                   model_uri=INCLUDEDCC.organism_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.subject_type = Slot(uri=INCLUDEDCC.subject_type, name="subject_type", curie=INCLUDEDCC.curie('subject_type'),
                   model_uri=INCLUDEDCC.subject_type, domain=None, range=Union[str, "EnumSubjectType"])

slots.sex = Slot(uri=INCLUDEDCC.sex, name="sex", curie=INCLUDEDCC.curie('sex'),
                   model_uri=INCLUDEDCC.sex, domain=None, range=Union[str, "EnumSex"])

slots.race = Slot(uri=INCLUDEDCC.race, name="race", curie=INCLUDEDCC.curie('race'),
                   model_uri=INCLUDEDCC.race, domain=None, range=Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]])

slots.ethnicity = Slot(uri=INCLUDEDCC.ethnicity, name="ethnicity", curie=INCLUDEDCC.curie('ethnicity'),
                   model_uri=INCLUDEDCC.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.down_syndrome_status = Slot(uri=INCLUDEDCC.down_syndrome_status, name="down_syndrome_status", curie=INCLUDEDCC.curie('down_syndrome_status'),
                   model_uri=INCLUDEDCC.down_syndrome_status, domain=None, range=Union[str, "EnumDownSyndromeStatus"])

slots.age_at_first_engagement = Slot(uri=INCLUDEDCC.age_at_first_engagement, name="age_at_first_engagement", curie=INCLUDEDCC.curie('age_at_first_engagement'),
                   model_uri=INCLUDEDCC.age_at_first_engagement, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=INCLUDEDCC.vital_status, name="vital_status", curie=INCLUDEDCC.curie('vital_status'),
                   model_uri=INCLUDEDCC.vital_status, domain=None, range=Optional[Union[str, "EnumVitalStatus"]])

slots.age_at_last_vital_status = Slot(uri=INCLUDEDCC.age_at_last_vital_status, name="age_at_last_vital_status", curie=INCLUDEDCC.curie('age_at_last_vital_status'),
                   model_uri=INCLUDEDCC.age_at_last_vital_status, domain=None, range=Optional[int])

slots.assertion_provenance = Slot(uri=INCLUDEDCC.assertion_provenance, name="assertion_provenance", curie=INCLUDEDCC.curie('assertion_provenance'),
                   model_uri=INCLUDEDCC.assertion_provenance, domain=None, range=Optional[Union[str, "EnumAssertionProvenance"]])

slots.age_at_assertion = Slot(uri=INCLUDEDCC.age_at_assertion, name="age_at_assertion", curie=INCLUDEDCC.curie('age_at_assertion'),
                   model_uri=INCLUDEDCC.age_at_assertion, domain=None, range=Optional[int])

slots.age_at_event = Slot(uri=INCLUDEDCC.age_at_event, name="age_at_event", curie=INCLUDEDCC.curie('age_at_event'),
                   model_uri=INCLUDEDCC.age_at_event, domain=None, range=Optional[int])

slots.age_at_resolution = Slot(uri=INCLUDEDCC.age_at_resolution, name="age_at_resolution", curie=INCLUDEDCC.curie('age_at_resolution'),
                   model_uri=INCLUDEDCC.age_at_resolution, domain=None, range=Optional[int])

slots.concept = Slot(uri=INCLUDEDCC.concept, name="concept", curie=INCLUDEDCC.curie('concept'),
                   model_uri=INCLUDEDCC.concept, domain=None, range=Optional[Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]])

slots.concept_curie = Slot(uri=INCLUDEDCC.concept_curie, name="concept_curie", curie=INCLUDEDCC.curie('concept_curie'),
                   model_uri=INCLUDEDCC.concept_curie, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.display = Slot(uri=INCLUDEDCC.display, name="display", curie=INCLUDEDCC.curie('display'),
                   model_uri=INCLUDEDCC.display, domain=None, range=Optional[str])

slots.concept_source = Slot(uri=INCLUDEDCC.concept_source, name="concept_source", curie=INCLUDEDCC.curie('concept_source'),
                   model_uri=INCLUDEDCC.concept_source, domain=None, range=Optional[str])

slots.value_concept = Slot(uri=INCLUDEDCC.value_concept, name="value_concept", curie=INCLUDEDCC.curie('value_concept'),
                   model_uri=INCLUDEDCC.value_concept, domain=None, range=Optional[Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]])

slots.value_number = Slot(uri=INCLUDEDCC.value_number, name="value_number", curie=INCLUDEDCC.curie('value_number'),
                   model_uri=INCLUDEDCC.value_number, domain=None, range=Optional[float])

slots.value_source = Slot(uri=INCLUDEDCC.value_source, name="value_source", curie=INCLUDEDCC.curie('value_source'),
                   model_uri=INCLUDEDCC.value_source, domain=None, range=Optional[str])

slots.value_unit = Slot(uri=INCLUDEDCC.value_unit, name="value_unit", curie=INCLUDEDCC.curie('value_unit'),
                   model_uri=INCLUDEDCC.value_unit, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.value_unit_source = Slot(uri=INCLUDEDCC.value_unit_source, name="value_unit_source", curie=INCLUDEDCC.curie('value_unit_source'),
                   model_uri=INCLUDEDCC.value_unit_source, domain=None, range=Optional[str])

slots.sample_id = Slot(uri=INCLUDEDCC.sample_id, name="sample_id", curie=INCLUDEDCC.curie('sample_id'),
                   model_uri=INCLUDEDCC.sample_id, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.parent_sample_id = Slot(uri=INCLUDEDCC.parent_sample_id, name="parent_sample_id", curie=INCLUDEDCC.curie('parent_sample_id'),
                   model_uri=INCLUDEDCC.parent_sample_id, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.biospecimen_collection_id = Slot(uri=INCLUDEDCC.biospecimen_collection_id, name="biospecimen_collection_id", curie=INCLUDEDCC.curie('biospecimen_collection_id'),
                   model_uri=INCLUDEDCC.biospecimen_collection_id, domain=None, range=Optional[Union[str, BiospecimenCollectionBiospecimenCollectionId]])

slots.aliquot_id = Slot(uri=INCLUDEDCC.aliquot_id, name="aliquot_id", curie=INCLUDEDCC.curie('aliquot_id'),
                   model_uri=INCLUDEDCC.aliquot_id, domain=None, range=Optional[Union[str, AliquotAliquotId]])

slots.sample_type = Slot(uri=INCLUDEDCC.sample_type, name="sample_type", curie=INCLUDEDCC.curie('sample_type'),
                   model_uri=INCLUDEDCC.sample_type, domain=None, range=Union[str, URIorCURIE])

slots.processing = Slot(uri=INCLUDEDCC.processing, name="processing", curie=INCLUDEDCC.curie('processing'),
                   model_uri=INCLUDEDCC.processing, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.availablity_status = Slot(uri=INCLUDEDCC.availablity_status, name="availablity_status", curie=INCLUDEDCC.curie('availablity_status'),
                   model_uri=INCLUDEDCC.availablity_status, domain=None, range=Optional[Union[str, "EnumAvailabilityStatus"]])

slots.storage_method = Slot(uri=INCLUDEDCC.storage_method, name="storage_method", curie=INCLUDEDCC.curie('storage_method'),
                   model_uri=INCLUDEDCC.storage_method, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.quantity_number = Slot(uri=INCLUDEDCC.quantity_number, name="quantity_number", curie=INCLUDEDCC.curie('quantity_number'),
                   model_uri=INCLUDEDCC.quantity_number, domain=None, range=Optional[float])

slots.quantity_unit = Slot(uri=INCLUDEDCC.quantity_unit, name="quantity_unit", curie=INCLUDEDCC.curie('quantity_unit'),
                   model_uri=INCLUDEDCC.quantity_unit, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.concentration_number = Slot(uri=INCLUDEDCC.concentration_number, name="concentration_number", curie=INCLUDEDCC.curie('concentration_number'),
                   model_uri=INCLUDEDCC.concentration_number, domain=None, range=Optional[float])

slots.concentration_unit = Slot(uri=INCLUDEDCC.concentration_unit, name="concentration_unit", curie=INCLUDEDCC.curie('concentration_unit'),
                   model_uri=INCLUDEDCC.concentration_unit, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.age_at_collection = Slot(uri=INCLUDEDCC.age_at_collection, name="age_at_collection", curie=INCLUDEDCC.curie('age_at_collection'),
                   model_uri=INCLUDEDCC.age_at_collection, domain=None, range=Optional[float])

slots.method = Slot(uri=INCLUDEDCC.method, name="method", curie=INCLUDEDCC.curie('method'),
                   model_uri=INCLUDEDCC.method, domain=None, range=Optional[Union[str, "EnumSampleCollectionMethod"]])

slots.site = Slot(uri=INCLUDEDCC.site, name="site", curie=INCLUDEDCC.curie('site'),
                   model_uri=INCLUDEDCC.site, domain=None, range=Optional[Union[str, "EnumSite"]])

slots.spatial_qualifier = Slot(uri=INCLUDEDCC.spatial_qualifier, name="spatial_qualifier", curie=INCLUDEDCC.curie('spatial_qualifier'),
                   model_uri=INCLUDEDCC.spatial_qualifier, domain=None, range=Optional[Union[str, "EnumSpatialQualifiers"]])

slots.laterality = Slot(uri=INCLUDEDCC.laterality, name="laterality", curie=INCLUDEDCC.curie('laterality'),
                   model_uri=INCLUDEDCC.laterality, domain=None, range=Optional[Union[str, "EnumLaterality"]])

slots.encounter_id = Slot(uri=INCLUDEDCC.encounter_id, name="encounter_id", curie=INCLUDEDCC.curie('encounter_id'),
                   model_uri=INCLUDEDCC.encounter_id, domain=None, range=Optional[Union[str, EncounterEncounterId]])

slots.description = Slot(uri=INCLUDEDCC.description, name="description", curie=INCLUDEDCC.curie('description'),
                   model_uri=INCLUDEDCC.description, domain=None, range=Optional[str])

slots.encounter_definition_id = Slot(uri=INCLUDEDCC.encounter_definition_id, name="encounter_definition_id", curie=INCLUDEDCC.curie('encounter_definition_id'),
                   model_uri=INCLUDEDCC.encounter_definition_id, domain=None, range=Optional[Union[str, EncounterDefinitionEncounterDefinitionId]])

slots.activity_definition_id = Slot(uri=INCLUDEDCC.activity_definition_id, name="activity_definition_id", curie=INCLUDEDCC.curie('activity_definition_id'),
                   model_uri=INCLUDEDCC.activity_definition_id, domain=None, range=Optional[Union[str, ActivityDefinitionActivityDefinitionId]])

slots.file_id = Slot(uri=INCLUDEDCC.file_id, name="file_id", curie=INCLUDEDCC.curie('file_id'),
                   model_uri=INCLUDEDCC.file_id, domain=None, range=Optional[Union[str, FileFileId]])

slots.filename = Slot(uri=INCLUDEDCC.filename, name="filename", curie=INCLUDEDCC.curie('filename'),
                   model_uri=INCLUDEDCC.filename, domain=None, range=Optional[str])

slots.format = Slot(uri=INCLUDEDCC.format, name="format", curie=INCLUDEDCC.curie('format'),
                   model_uri=INCLUDEDCC.format, domain=None, range=Optional[Union[str, "EnumEDAMFormats"]])

slots.data_type = Slot(uri=INCLUDEDCC.data_type, name="data_type", curie=INCLUDEDCC.curie('data_type'),
                   model_uri=INCLUDEDCC.data_type, domain=None, range=Optional[Union[str, "EnumEDAMDataTypes"]])

slots.size = Slot(uri=INCLUDEDCC.size, name="size", curie=INCLUDEDCC.curie('size'),
                   model_uri=INCLUDEDCC.size, domain=None, range=Optional[int])

slots.staging_url = Slot(uri=INCLUDEDCC.staging_url, name="staging_url", curie=INCLUDEDCC.curie('staging_url'),
                   model_uri=INCLUDEDCC.staging_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.release_url = Slot(uri=INCLUDEDCC.release_url, name="release_url", curie=INCLUDEDCC.curie('release_url'),
                   model_uri=INCLUDEDCC.release_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.drs_uri = Slot(uri=INCLUDEDCC.drs_uri, name="drs_uri", curie=INCLUDEDCC.curie('drs_uri'),
                   model_uri=INCLUDEDCC.drs_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.hash = Slot(uri=INCLUDEDCC.hash, name="hash", curie=INCLUDEDCC.curie('hash'),
                   model_uri=INCLUDEDCC.hash, domain=None, range=Optional[Union[dict, FileHash]])

slots.hash_type = Slot(uri=INCLUDEDCC.hash_type, name="hash_type", curie=INCLUDEDCC.curie('hash_type'),
                   model_uri=INCLUDEDCC.hash_type, domain=None, range=Optional[Union[str, "EnumFileHashType"]])

slots.hash_value = Slot(uri=INCLUDEDCC.hash_value, name="hash_value", curie=INCLUDEDCC.curie('hash_value'),
                   model_uri=INCLUDEDCC.hash_value, domain=None, range=Optional[str])

slots.dataset_id = Slot(uri=INCLUDEDCC.dataset_id, name="dataset_id", curie=INCLUDEDCC.curie('dataset_id'),
                   model_uri=INCLUDEDCC.dataset_id, domain=None, range=Optional[Union[str, DatasetDatasetId]])

slots.data_collection_start = Slot(uri=INCLUDEDCC.data_collection_start, name="data_collection_start", curie=INCLUDEDCC.curie('data_collection_start'),
                   model_uri=INCLUDEDCC.data_collection_start, domain=None, range=Optional[str])

slots.data_collection_end = Slot(uri=INCLUDEDCC.data_collection_end, name="data_collection_end", curie=INCLUDEDCC.curie('data_collection_end'),
                   model_uri=INCLUDEDCC.data_collection_end, domain=None, range=Optional[str])

slots.Study_study_id = Slot(uri=INCLUDEDCC.study_id, name="Study_study_id", curie=INCLUDEDCC.curie('study_id'),
                   model_uri=INCLUDEDCC.Study_study_id, domain=Study, range=Union[str, StudyStudyId])

slots.StudyMetadata_study_id = Slot(uri=INCLUDEDCC.study_id, name="StudyMetadata_study_id", curie=INCLUDEDCC.curie('study_id'),
                   model_uri=INCLUDEDCC.StudyMetadata_study_id, domain=StudyMetadata, range=Union[str, StudyMetadataStudyId])

slots.StudyMetadata_data_category = Slot(uri=INCLUDEDCC.data_category, name="StudyMetadata_data_category", curie=INCLUDEDCC.curie('data_category'),
                   model_uri=INCLUDEDCC.StudyMetadata_data_category, domain=StudyMetadata, range=Union[Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]])

slots.VirtualBiorepository_vbr_id = Slot(uri=INCLUDEDCC.vbr_id, name="VirtualBiorepository_vbr_id", curie=INCLUDEDCC.curie('vbr_id'),
                   model_uri=INCLUDEDCC.VirtualBiorepository_vbr_id, domain=VirtualBiorepository, range=Union[str, VirtualBiorepositoryVbrId])

slots.DOI_do_id = Slot(uri=INCLUDEDCC.do_id, name="DOI_do_id", curie=INCLUDEDCC.curie('do_id'),
                   model_uri=INCLUDEDCC.DOI_do_id, domain=DOI, range=Union[str, DOIDoId])

slots.Subject_subject_id = Slot(uri=INCLUDEDCC.subject_id, name="Subject_subject_id", curie=INCLUDEDCC.curie('subject_id'),
                   model_uri=INCLUDEDCC.Subject_subject_id, domain=Subject, range=Union[str, SubjectSubjectId])

slots.Demographics_subject_id = Slot(uri=INCLUDEDCC.subject_id, name="Demographics_subject_id", curie=INCLUDEDCC.curie('subject_id'),
                   model_uri=INCLUDEDCC.Demographics_subject_id, domain=Demographics, range=Union[str, DemographicsSubjectId])

slots.SubjectAssertion_assertion_id = Slot(uri=INCLUDEDCC.assertion_id, name="SubjectAssertion_assertion_id", curie=INCLUDEDCC.curie('assertion_id'),
                   model_uri=INCLUDEDCC.SubjectAssertion_assertion_id, domain=SubjectAssertion, range=Union[str, SubjectAssertionAssertionId])

slots.Concept_concept_curie = Slot(uri=INCLUDEDCC.concept_curie, name="Concept_concept_curie", curie=INCLUDEDCC.curie('concept_curie'),
                   model_uri=INCLUDEDCC.Concept_concept_curie, domain=Concept, range=Union[str, ConceptConceptCurie])

slots.Sample_sample_id = Slot(uri=INCLUDEDCC.sample_id, name="Sample_sample_id", curie=INCLUDEDCC.curie('sample_id'),
                   model_uri=INCLUDEDCC.Sample_sample_id, domain=Sample, range=Union[str, SampleSampleId])

slots.Sample_biospecimen_collection_id = Slot(uri=INCLUDEDCC.biospecimen_collection_id, name="Sample_biospecimen_collection_id", curie=INCLUDEDCC.curie('biospecimen_collection_id'),
                   model_uri=INCLUDEDCC.Sample_biospecimen_collection_id, domain=Sample, range=Optional[Union[str, BiospecimenCollectionBiospecimenCollectionId]])

slots.BiospecimenCollection_biospecimen_collection_id = Slot(uri=INCLUDEDCC.biospecimen_collection_id, name="BiospecimenCollection_biospecimen_collection_id", curie=INCLUDEDCC.curie('biospecimen_collection_id'),
                   model_uri=INCLUDEDCC.BiospecimenCollection_biospecimen_collection_id, domain=BiospecimenCollection, range=Union[str, BiospecimenCollectionBiospecimenCollectionId])

slots.Aliquot_aliquot_id = Slot(uri=INCLUDEDCC.aliquot_id, name="Aliquot_aliquot_id", curie=INCLUDEDCC.curie('aliquot_id'),
                   model_uri=INCLUDEDCC.Aliquot_aliquot_id, domain=Aliquot, range=Union[str, AliquotAliquotId])

slots.Encounter_encounter_id = Slot(uri=INCLUDEDCC.encounter_id, name="Encounter_encounter_id", curie=INCLUDEDCC.curie('encounter_id'),
                   model_uri=INCLUDEDCC.Encounter_encounter_id, domain=Encounter, range=Union[str, EncounterEncounterId])

slots.EncounterDefinition_encounter_definition_id = Slot(uri=INCLUDEDCC.encounter_definition_id, name="EncounterDefinition_encounter_definition_id", curie=INCLUDEDCC.curie('encounter_definition_id'),
                   model_uri=INCLUDEDCC.EncounterDefinition_encounter_definition_id, domain=EncounterDefinition, range=Union[str, EncounterDefinitionEncounterDefinitionId])

slots.EncounterDefinition_activity_definition_id = Slot(uri=INCLUDEDCC.activity_definition_id, name="EncounterDefinition_activity_definition_id", curie=INCLUDEDCC.curie('activity_definition_id'),
                   model_uri=INCLUDEDCC.EncounterDefinition_activity_definition_id, domain=EncounterDefinition, range=Optional[Union[Union[str, ActivityDefinitionActivityDefinitionId], list[Union[str, ActivityDefinitionActivityDefinitionId]]]])

slots.ActivityDefinition_activity_definition_id = Slot(uri=INCLUDEDCC.activity_definition_id, name="ActivityDefinition_activity_definition_id", curie=INCLUDEDCC.curie('activity_definition_id'),
                   model_uri=INCLUDEDCC.ActivityDefinition_activity_definition_id, domain=ActivityDefinition, range=Union[str, ActivityDefinitionActivityDefinitionId])

slots.File_file_id = Slot(uri=INCLUDEDCC.file_id, name="File_file_id", curie=INCLUDEDCC.curie('file_id'),
                   model_uri=INCLUDEDCC.File_file_id, domain=File, range=Union[str, FileFileId])

slots.File_subject_id = Slot(uri=INCLUDEDCC.subject_id, name="File_subject_id", curie=INCLUDEDCC.curie('subject_id'),
                   model_uri=INCLUDEDCC.File_subject_id, domain=File, range=Optional[Union[Union[str, SubjectSubjectId], list[Union[str, SubjectSubjectId]]]])

slots.File_sample_id = Slot(uri=INCLUDEDCC.sample_id, name="File_sample_id", curie=INCLUDEDCC.curie('sample_id'),
                   model_uri=INCLUDEDCC.File_sample_id, domain=File, range=Optional[Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]])

slots.Dataset_dataset_id = Slot(uri=INCLUDEDCC.dataset_id, name="Dataset_dataset_id", curie=INCLUDEDCC.curie('dataset_id'),
                   model_uri=INCLUDEDCC.Dataset_dataset_id, domain=Dataset, range=Union[str, DatasetDatasetId])

slots.Dataset_file_id = Slot(uri=INCLUDEDCC.file_id, name="Dataset_file_id", curie=INCLUDEDCC.curie('file_id'),
                   model_uri=INCLUDEDCC.Dataset_file_id, domain=Dataset, range=Optional[Union[Union[str, FileFileId], list[Union[str, FileFileId]]]])
