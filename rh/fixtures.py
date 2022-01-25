# -*- coding: utf-8 -*-
#  Si Hay Sistema and Contributors 2021
from __future__ import unicode_literals


def fill_fixtures():
    fixtures_fillup = []

    custom_fields = {
        "dt": "Custom Field", "filters": [
            [
                "name", "in", [
                    "Job Opening-personality_profile", "Job Applicant-big_five_results",
                    "Job Applicant-recommended_profile", "Job Opening-rh_gender",
                    "Job Opening-rh_job_location", "Job Opening-rh_employment_status"
                ]
            ]
        ]
    }

    translation = {
        "dt": "Translation", "filters": [
            [
                "source_text", "in", [
                    "de", "fueron respondidas, por favor responda todas las preguntas y presione completar",
                    "Psychometric Tests", "Questions", "Big Five Factor Model", "Results", "Big Five Results",
                    "Date Time", "EXTRAVERSION", "AGREEABLENESS", "CONSCIENTIOUSNESS", "NEUROTICISM", "OPENNESS",
                    "COMPLETE", "POS", "Am the life of the party.", "Feel comfortable around people.",
                    "Start conversations.", "Talk to a lot of different people at parties.",
                    "Don't mind being the center of attention.", "Make friends easily.", "Take charge.",
                    "Know how to captivate people.", "Feel at ease with people.", "Am skilled in handling social situations.",
                    "Don't talk a lot.", "Keep in the background.", "Have little to say.", "Don't like to draw attention to myself.",
                    "Am quiet around strangers.", "Find it difficult to approach others.", "Often feel uncomfortable around others.",
                    "Bottle up my feelings.", "Am a very private person.", "Wait for others to lead the way.",
                    "Am interested in people.", "Sympathize with others' feelings.", "Have a soft heart.",
                    "Take time out for others.", "Feel others' emotions.", "Make people feel at ease.",
                    "Inquire about others' well-being.", "Know how to comfort others.", "Love children.",
                    "Am on good terms with nearly everyone.", "Have a good word for everyone.", "Show my gratitude.",
                    "Think of others first.", "Love to help others.", "Insult people.", "Am not interested in other people's problems.",
                    "Feel little concern for others.", "Am not really interested in others.", "Am hard to get to know.",
                    "Am indifferent to the feelings of others.", "Am always prepared.", "Pay attention to details.",
                    "Get chores done right away.", "Like order.", "Follow a schedule.", "Am exacting in my work.",
                    "Do things according to a plan.", "Continue until everything is perfect.", "Make plans and stick to them.",
                    "Love order and regularity.", "Like to tidy up.", "Leave my belongings around.", "Make a mess of things.",
                    "Often forget to put things back in their proper place.", "Shirk my duties.", "Neglect my duties.",
                    "Waste my time.", "Do things in a half-way manner.", "Find it difficult to get down to work.",
                    "Leave a mess in my room.", "Am relaxed most of the time.", "Seldom feel blue.",
                    "Am not easily bothered by things.", "Rarely get irritated.", "Seldom get mad.", "Get stressed out easily.",
                    "Worry about things.", "Am easily disturbed.", "Get upset easily.", "Change my mood a lot.",
                    "Have frequent mood swings.", "Get irritated easily.", "Often feel blue.", "Get angry easily.",
                    "Panic easily.", "Feel threatened easily.", "Get overwhelmed by emotions.", "Take offense easily.",
                    "Get caught up in my problems.", "Grumble about things.", "Have a rich vocabulary.", "Have a vivid imagination.",
                    "Have excellent ideas.", "Am quick to understand things.", "Use difficult words.", "Spend time reflecting on things.",
                    "Am full of ideas.", "Carry the conversation to a higher level.", "Catch on to things quickly.",
                    "Can handle a lot of information.", "Love to think up new ways of doing things.", "Love to read challenging material.",
                    "Am good at many things.", "Have difficulty understanding abstract ideas.", "Am not interested in abstract ideas.",
                    "Do not have a good imagination.", "Try to avoid complex people.", "Have difficulty imagining things.",
                    "Avoid difficult reading material.", "Will not probe deeply into a subject.", "Very Inaccurate",
                    "Moderately Inaccurate", "Neither Inaccurate nor Accurate", "Moderately Accurate", "Very Accurate",
                    "Test Completed By", "Date and Time", "Personality Profile", "Big Five Parameters", "Minimum Result for Extraversion",
                    "Maximum Result for Extraversion", "Minimum Result for Agreeableness", "Maximun Result for Agreeableness",
                    "Minimum Result for Conscientiousness", "Maximun Result for Conscientiousness", "Minimum Result for Neuroticism",
                    "Maximun Result for Neuroticism", "Minimum Result for Openness", "Maximun Result for Openness", "Employment Status",
                    "RH: Select a profile", "Job Location", "RH - Example: Guatemala", "Completed From", "Recommended Profiles", "Profile"
                ]
            ]
        ]
    }

    big_five_factor_model = {
        "dt": "Big Five Factor Model"
    }

    fixtures_fillup.append(custom_fields)
    fixtures_fillup.append(translation)
    fixtures_fillup.append(big_five_factor_model)

    return fixtures_fillup
