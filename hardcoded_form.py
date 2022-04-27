#!/usr/bin/env python3.10

## generate a one-off hard coded form document

from random import randint
from typing import Union

import arrow

from client_data import google_analytics_id, maintainer_email, maintainer_id, organization_id

# Other schemas we might want to use:
# Action, FormFieldValidation, FormLogic, JumpCondition, JumpDetails, JumpTo, JumpVars, OpinionScaleLabels, OpinionScaleProperties,
from form_schema import (
    Choice,
    DropDownProperties,
    Form,
    FormField,
    FormLinks,
    FormMeta,
    FormSettingNotification,
    FormSettingNotifications,
    FormSettings,
    FormStructure,
    MultipleChoiceProperties,
    Screen,
    ScreenProperties,
)


def create_hardcoded_form(return_type: str = 'dictionary') -> Union[dict, str, Form]:

    form_meta = FormMeta(creator_id=maintainer_id, updater_id=maintainer_id, creator_email=maintainer_email, updater_email=maintainer_email)

    form_links = FormLinks()

    drop_down_properties = DropDownProperties(
        alphabetical_order=False,
        choices=[
            Choice(ref='a', label='pick me first'),
            Choice(ref='b', label='this is a good second choice'),
            Choice(ref='c', label='is this the third option?'),
        ],
        randomize=False,
    )

    multiple_choice_properties = MultipleChoiceProperties(
        allow_multiple_selection=True,
        allow_other_choice=True,
        choices=[
            Choice(ref='multi-a', label='pick me first'),
            Choice(ref='multi-b', label='this is a good second choice'),
            Choice(ref='multi-c', label='is this the third option?'),
            Choice(ref='multi-d', label='you know it'),
        ],
        randomize=False,
        vertical_alignment=True,
    )

    form_fields = [
        FormField(
            properties=drop_down_properties,
            ref='test drop down',
            title='drop this down',
            type='dropdown',
        ),
        FormField(
            properties=multiple_choice_properties,
            ref='test pick one',
            title='multiple choice question',
            type='multiple_choice',
        ),
    ]

    form_setting_notification_self = FormSettingNotification(
        enabled=True,
        message='Your {{form:title}} has a new response\n\n{{form:all_answers}}',
        subject='New response for {{form:title}} ',
        recipients=[maintainer_email],
    )

    form_setting_notification_respondent = FormSettingNotification(
        enabled=True,
        message='Hello,\nWe\u2019ve received your submission.\n{{form:all_answers}}\nThank you & have a nice day!',
        subject='Thank you for filling out {{form:title}}',
        recipients=[maintainer_email],
    )

    form_setting_notifications = FormSettingNotifications(self=form_setting_notification_self, respondent=form_setting_notification_respondent)

    form_settings = FormSettings(
        google_analytics=google_analytics_id,
        notifications=form_setting_notifications,
        progress_bar='percentage',
    )

    thank_you_screen_properties = ScreenProperties(
        button_mode='redirect',
        button_text='Would you like to join the Menstrual Movement?',
        redirect_url='https://dashboard-beaconstac-21449743.hubspotpagebuilder.com/join-the-menstrual-movement',
    )

    thank_you_screen = Screen(ref='thankyou-screen', title='Done! We appreciate your feedback.', properties=thank_you_screen_properties)

    welcome_screen_properties = ScreenProperties(
        button_text='start it up',
    )

    welcome_screen = Screen(ref='welcome-screen', title='Tell us your feedback!', properties=welcome_screen_properties)

    form_structure = FormStructure(
        _links=form_links,
        fields=form_fields,
        hidden=[],
        logic=[],
        settings=form_settings,
        thankyou_screens=[thank_you_screen],
        title='how is this different from the title field in Form?',
        type='quiz',
        welcome_screens=[welcome_screen],
    )

    form = Form(
        beacons=[],
        created=arrow.now().datetime,
        default=False,
        email_structure={},
        form_structure=form_structure,
        form_type='TY',
        maintainer=maintainer_id,
        meta=form_meta,
        organization=organization_id,
        sms_structure={},
        threat_active=False,
        title=f'Our Test Form - {randint(1,1000)}',
        updated=arrow.now().datetime,
    )

    if return_type == 'dictionary':
        return form.dict(exclude_unset=True)
    elif return_type == 'json':
        return form.json(exclude_unset=True)
    else:
        return form
