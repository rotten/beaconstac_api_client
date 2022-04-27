#!/usr/bin/env python3.10

## Pydantic schema components defining the shape of the forms json.

# todo:  set up some enums for the fields with discrete values

from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class FormMeta(BaseModel):
    creator_id: int
    updater_id: int
    creator_email: str
    updater_email: str


class FormLinks(BaseModel):
    display: Optional[str]  # same as Form.url


class FormSettingNotification(BaseModel):
    enabled: bool
    message: str
    subject: str
    recipients: list[str]


class FormSettingNotifications(BaseModel):
    self: FormSettingNotification
    respondent: FormSettingNotification


class FormSettings(BaseModel):
    are_uploads_public: bool = False
    capabilities: dict = {'e2e_encryption': {'enabled': False, 'modifiable': False}}
    google_analytics: str
    hide_navigation: bool = False
    is_public: bool = False
    is_trial: bool = False
    language: str = 'en'
    meta: dict = {'allow_indexing': False}
    notifications: FormSettingNotifications
    pro_subdomain_enabled: bool = False
    progress_bar: str  # 'percentage'
    show_number_of_submissions: bool = False
    show_progress_bar: bool = True
    show_time_to_complete: bool = True
    show_typeform_branding: bool = True


class Choice(BaseModel):
    id: Optional[str]
    ref: str
    label: str


class DropDownProperties(BaseModel):
    alphabetical_order: bool
    choices: list[Choice]
    randomize: bool


class MultipleChoiceProperties(BaseModel):
    allow_multiple_selection: bool
    allow_other_choice: bool
    choices: list[Choice]
    randomize: bool
    vertical_alignment: Optional[bool]


class OpinionScaleLabels(BaseModel):
    left: str
    right: str
    center: str


class OpinionScaleProperties(BaseModel):
    labels: OpinionScaleLabels
    start_at_one: bool
    steps: int


class FormFieldValidation(BaseModel):
    required: bool


class FormField(BaseModel):
    id: Optional[str]
    properties: Union[DropDownProperties, MultipleChoiceProperties, OpinionScaleProperties]
    ref: str
    title: str
    type: str  # 'dropdown', 'multiple_choice', 'opinion_scale', 'long_text', 'statement', 'short_text'
    validations: Optional[FormFieldValidation]


class JumpTo(BaseModel):
    type: str  # 'field'
    value: str


class JumpDetails(BaseModel):
    to: JumpTo


class JumpVars(BaseModel):
    type: str  # 'field', 'constant'
    value: str


class JumpCondition(BaseModel):
    op: str   # 'equal', 'always'
    vars: list[JumpVars]


class Action(BaseModel):
    action: str  # 'jump'
    details: JumpDetails
    condition: JumpCondition


class FormLogic(BaseModel):
    actions: list[Action]
    ref: str
    type: str  # 'field'


class ScreenProperties(BaseModel):
    button_mode: Optional[str]  # redirect
    button_text: Optional[str]
    description: Optional[str]
    redirect_url: Optional[str]
    share_icons: bool = False
    show_button: bool = True


class Screen(BaseModel):
    id: Optional[str]
    properties: ScreenProperties
    ref: str
    title: str


class FormStructure(BaseModel):
    _links: FormLinks
    fields: list[FormField]
    hidden: list[str]  # hidden field names
    id: Optional[str]
    logic: list[FormLogic]
    settings: FormSettings
    thankyou_screens: list[Screen]
    theme: dict = {'href': 'https://api.typeform.com/themes/MxFuG7'}
    title: str
    type: str  # 'quiz'
    variables: dict = {'score': 0}
    welcome_screens: list[Screen]
    workspace: dict = {'href': 'https://api.typeform.com/workspaces/11932656'}


class Form(BaseModel):
    beacons: list = []
    created: datetime
    default: bool
    email_structure: dict = {}
    form_id: Optional[str]
    form_response_count: Optional[int]
    form_structure: FormStructure
    form_type: str  # 'TY'
    id: Optional[int]
    maintainer: int
    meta: FormMeta
    organization: int
    sms_structure: dict = {}
    threat_active: bool
    title: str
    url: Optional[str]
    updated: datetime
