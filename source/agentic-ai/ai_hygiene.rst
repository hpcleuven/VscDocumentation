.. _ai_hygiene:

AI hygiene
==========

Whether you integrate your AI tools locally (and access HPC resources remotely), or you
deploy them directly on the VSC cloud and/or compute platforms, you are recognized
as the end-responsible party for the outcome and consequences of using AI tools.

To ensure a safe and responsible use of AI tools, it is important that the user
keeps control over specific aspects. Concretely speaking,

* you need to comply with the `institutional AI policies <ai_charters>`_,
* you are expected to beware of AI security aspects and practice safe AI usage,
* you need to stay as a `human in the loop <human_in_the_loop>`_ to surveil every step
  that AI tools plan to take
* you only use trusted AI components from public sources

Below, we elaborate further on some of these aspects.


.. _confidentiality_and_ai:

Confidentiality and AI
----------------------

A user may need to process sensitive or confidential information, such as non-anonymized
patient data, financial records, patented designs and alike.
In all respects, your intellectual property (which also belongs to your funding institution/agency)
must be protected by all means, preventing any unauthorized access or leakage through AI tools.
The first step in such scenarios is to anonymize or pseudonymize the sensitive data in
an environment which is isolated from any AI tool.

To treat sensitive data with AI tools, it is crucial to ensure that the AI tools comply
with data protection and privacy regulations of your host institution and/or research
department.
In other terms, users have to ensure that their sensitive data and source code - in any form -
is not transferred to unauthorized parties or external systems such as cloud services.
In this regard, 

.. warning::

    Using free/trial versions of unlicensed AI tools on VSC systems is strictly prohibited.

    Even licensed AI tools should be carefully evaluated for their terms and conditions of
    data handling before using them with sensitive data.


.. _human_in_the_loop:

Human in the loop
-----------------

AI agents shine when it comes to autonomy.
Concretely, AI agents are capable of executing any command they come up with in a given context.
But, imagine that such a command would be to delete or overwrite sensitive files without the
user's explicit consent; depending on the backup/recovery mechanism of the host filesystem,
such changes maybe irreversible.

However, when a human is in the loop, the execution of risky commands will be performed after an
explicit consent from the end user.
In the previous example, the user can prevent the loss of valuable content by disallowing the
execution of the risky command by the AI agent.

As an another example, an AI coding assistant can draft a reasonable piece of code based on
the user's prompt.
The agent may assume he can write temporary files under ``/tmp``.
However, the quota of ``/tmp`` directory on most VSC systems is limited by intention, 
leading to the crash of the code or even the slave compute node at runtime.
Given the shared user policy of compute nodes, such a flaw can also break other concurrently-running
processes on the same node from other VSC users.
With a human in the loop, the end user spots potential issues and instructs the AI agent to
make use of the user's storage, instead.

[For Reviewers] Does ``/tmp`` on all clusters compute nodes point at ``$VSC_SCRATCH_NODE``?
In Leuven it does, but not sure about other sites.
If the ``/tmp`` is a bad example, I will take it out.

As a good practice,

* do not permit the AI agent to autonomously execute any command without your explicit consent.
  If you use IDEs, make sure to configure them to inquire your explicit confirmation
  before executing any commands suggested by the AI agent.

  You must opt for harnessing your AI agents through ``SKILL.md`` or ``AGENTS.md``
  files and/or MCP (Model Control Protocol) servers.
  But, AI agents may still overstep the harnesses by attempting to execute commands
  beyond the granted permissions.

  [For Reviewers: We either have to elaborate on skills/MCP or provide links to some external
  educational resources. Else, this best-practice tip hangs pretty loose here and raises more
  questions/confusion than providing concrete answers to doubts].

* review and validate each and every action suggested by the AI agent before allowing execution.
* spot the critical operations (such as file deletions) or possible file overwrites.


.. _ai_public_tools:

Public AI tools
---------------

The `components of AI tools <ai_components>`_ are developed and maintained independent from one another,
and are made publically available in an ever-growing ecosystem.
Normally, each of these components are hosted by well-recognized hubs; for instance, many LLMs
are hosted by `huggingface`_ or `ollama`_ and similar platforms.
If even one of the `components of your AI toolkit <ai_components>`_ is compromised or contains
vulnerabilities, it can have serious security implications for the system on which the AI tools 
are deployed.

.. warning::

    VSC users are strongly advised to carefully assess and verify the security and
    integrity of each component before integrating them into their AI toolkiti.
    That implies pulling each component of their AI toolkit from trusted sources.


Furthermore, the user should fully surveil the behavior and interactions of each component
with the system where they are deployed.
Additionally, one needs to stay updated with the latest security advisories and patches
related to the AI models and tools he/she uses.


.. _ai_agent_orchestration:

AI agent orchestration
----------------------

Orchestrating AI agents involves coordinating multiple agents to work together effectively.
It is crucial to ensure that all agents are harnessed properly, and that each agent operates
within its designated boundaries and follows the security and operational guidelines set by
the user.
Proper orchestration helps prevent conflicts, redundancy, resource contention, and 
unintended actions that could compromise the system's integrity or other users' workflows.


.. _ai_and_credentials:

AI and credentials
-------------------

When using AI tools, it is essential to handle credentials with utmost care.
Avoid hardcoding sensitive information such as passwords, API keys, or access tokens
directly into your code or AI agent configurations.
Instead, use secure credential management systems, vaults, or environment variables
to store and access sensitive information.
Regularly rotate credentials and monitor their usage to detect any unauthorized access.
Ensuring proper credential hygiene helps mitigate the risk of security breaches and
protects the integrity of your HPC environment.