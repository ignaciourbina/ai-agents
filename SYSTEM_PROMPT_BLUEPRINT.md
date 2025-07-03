# Section 2: The Blueprint for a High-Performance System Prompt

While every AI task requires a unique prompt, the underlying architecture of a state-of-the-art prompt follows a predictable pattern. Moving beyond simple instructions to a structured, multi-component "briefing" for the AI is the key to unlocking reliable, consistent, and high-quality performance.

This section provides a universal template for constructing such prompts. It is designed as a "prompt for writing prompts"—a blueprint you can copy, paste, and fill in to ensure you incorporate all the critical elements that separate an amateur instruction from a professional system prompt.

## The Universal Prompt Template

```
# ====================================================================
# SYSTEM PROMPT BLUEPRINT
# ====================================================================

# 1. ROLE & MISSION
# =================
# You are [AGENT_NAME], a specialized AI assistant for [AREA_OF_EXPERTISE].
# Your primary mission is to [PRIMARY_OBJECTIVE] by analyzing user-provided
# input and generating [TYPE_OF_OUTPUT].

# 2. KNOWLEDGE & CONTEXT
# ======================
# You will base your analysis and output exclusively on the following sources:
#   1. The user-provided text in the current prompt.
#   2. [OPTIONAL: Specify any guiding documents, frameworks, or principles, e.g., "The principles outlined in the 'XYZ Style Guide'."]
#   3. [OPTIONAL: Specify any other relevant context.]

# 3. CORE FRAMEWORK / WORKFLOW
# ============================
# Follow this exact sequence of steps to fulfill your mission:
#   1. [First, analyze/scan/review the user's input for key elements...]
#   2. [Second, categorize/extract/evaluate the information based on these criteria...]
#   3. [Third, synthesize the findings and construct the response by...]
#   4. [Finally, review the generated output against the constraints before finishing.]

# 4. OUTPUT FORMAT & STRUCTURE
# ============================
# Your final output MUST be structured in the following format. Do not
# include any conversational text, apologies, or explanations outside of
# this structure.
#
# [Provide a clear, skeletal structure of the desired output. Use markdown,
#  XML tags, or a JSON schema. Be explicit.]
#
# --- EXAMPLE OUTPUT STRUCTURE ---
# <analysis>
#   <finding type="[Category A]">
#     <quote>[Relevant quote from source]</quote>
#     <diagnosis>[Your one-sentence diagnosis]</diagnosis>
#     <recommendation>[Your one-sentence fix]</recommendation>
#   </finding>
#   <finding type="[Category B]">
#     ...
#   </finding>
# </analysis>
# --- END EXAMPLE ---


# 5. CONSTRAINTS & GUARDRAILS
# ===========================
# Adhere to these hard rules at all times:
#   ✓ **DO:** [A positive, mandatory action, e.g., "Quote directly from the source text for every finding."]
#   ✓ **DO:** [Another positive, mandatory action.]
#   ✗ **DO NOT:** [A negative, forbidden action, e.g., "Do not invent information or make assumptions beyond the provided text."]
#   ✗ **DO NOT:** [Another negative, forbidden action, e.g., "Do not output any text after the final closing tag."]

# 6. EXAMPLE (FEW-SHOT PROMPT)
# ============================
# To ensure perfect execution, here is a micro-example of the complete
# workflow from input to output.
#
# --- START EXAMPLE ---
# USER INPUT:
# "[Provide a concise, representative example of what the user will provide.]"
#
# YOUR OUTPUT:
# "[Provide the perfect, corresponding output that follows every rule and
#  matches the format defined in Section 4.]"
# --- END EXAMPLE ---
```

Anatomy of the Blueprint
Each section of the template serves a critical function rooted in established prompt engineering best practices.
1. ROLE & MISSION: This is the foundation. By assigning a specific persona and a clear objective (You are a specialized legal analyst...), you move the AI from a generalist model to a focused specialist. This dramatically improves the tone, relevance, and quality of the output.
2. KNOWLEDGE & CONTEXT: This section builds a "fence" around the information the AI is allowed to use. Specifying its knowledge base prevents it from drawing on its vast, generic training data and forces it to ground its responses in the context you provide, which is the single most effective way to reduce hallucinations.
3. CORE FRAMEWORK / WORKFLOW: This implements the "Chain of Thought" principle. By defining a clear, sequential workflow, you force the model to "think step-by-step." This breaks down complex tasks into manageable chunks, leading to more logical, accurate, and reliable reasoning.
4. OUTPUT FORMAT & STRUCTURE: This is where you eliminate ambiguity in the final deliverable. Providing a rigid schema—whether with XML tags, Markdown, or JSON—is far more effective than describing the format in prose. The model can match the pattern precisely, making the output predictable and machine-readable.
5. CONSTRAINTS & GUARDRAILS: This section sets the hard rules. Explicitly stating what the model must do and, just as importantly, what it must not do acts as a final layer of control. Negative constraints (DO NOT...) are particularly powerful for preventing common failure modes like adding conversational fluff or breaking the output format.
6. EXAMPLE (FEW-SHOT PROMPT): This is arguably the most powerful component. While the other sections describe the task, the example demonstrates it. Providing a single, high-quality example of a perfect input-output pair allows the model to learn by imitation, often leading to a greater leap in quality than any other part of the prompt.

