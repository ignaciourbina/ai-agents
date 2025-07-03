# Section 1: The State of the Art in Prompt Engineering, According to Anthropic

Prompt engineering, at its core, is the practice of designing effective instructions to guide AI models toward desired outcomes. According to Anthropic, the creators of the Claude family of models, this practice has evolved far beyond simple questions and commands. State-of-the-art prompting is a discipline of structure, clarity, and context. It treats the AI not as a conversationalist, but as a highly capable, newly-hired team member who requires a clear and thorough job briefing to perform at their best. Drawing directly from Anthropic's official documentation and tutorials, here are the foundational techniques that define expert-level prompt design.

## 1. Be Clear, Direct, and Specific

The most fundamental principle is to eliminate ambiguity. Models like Claude perform best when instructions are direct and detailed. Instead of telling the model what not to do, it is more effective to provide affirmative instructions on what it should do.
- **Ineffective (Vague):** "Summarize the attached text."
- **Effective (Specific):** "Summarize the attached article in three bullet points, focusing on its financial implications. The target audience is a group of senior executives."

## 2. Use XML Tags to Structure the Prompt

A cornerstone of prompting Claude models is the use of XML-style tags (e.g., <doc>, </doc>) to delineate different parts of the prompt. Claude has been specifically fine-tuned to recognize this structure, allowing it to clearly separate instructions from context, examples from input data, and so on. You can invent any tag names you like; the structure is what matters. This is the recommended way to provide complex information.

```
<instructions>
Summarize the document within the <document> tags.
Extract the key person mentioned and place their name in <person> tags.
</instructions>

<document>
The quarterly report was presented by CEO Jane Doe. She highlighted a 15% growth
in the tech sector and outlined future strategies.
</document>
```

## 3. Assign a Role or Persona

You can significantly improve a model's performance by assigning it a role at the beginning of the prompt. This helps set the appropriate tone, vocabulary, and level of expertise for the response.
Example: "You are an expert legal analyst specializing in contract law. Review the following clause and identify any potential ambiguities."
This technique focuses the model's vast knowledge, leading to more consistent and higher-quality output that aligns with the specified character.

## 4. Let the Model "Think" with Chain-of-Thought

For complex tasks that require reasoning, forcing the model to "think step-by-step" before providing a final answer dramatically reduces errors. This is often called a "chain of thought" or "scratchpad" method. You instruct the model to work through its reasoning within a dedicated set of XML tags, which you can then choose to display or ignore in the final output.
Example: "Please answer the user's question. First, in <thinking> tags, pull the most relevant quotes from the provided document and analyze how they relate to the question. After your thinking process, provide the final answer inside <answer> tags."
This makes the model's reasoning process transparent and forces a more deliberate analysis, leading to more accurate results.

## 5. Show, Don't Just Tell: Use Examples (Few-Shot Prompting)

One of the most powerful ways to guide a model is to provide examples of the desired output format and content. Providing three to five high-quality, relevant examples (a technique known as "few-shot prompting") helps the model understand patterns and replicate them accurately.
Example: "Extract the company name and product from the following sentences. Follow the JSON format of the examples.
- **Example 1:**
  - Text: "Innovate Inc. just launched the new TurboWidget."
  - JSON: {"company": "Innovate Inc.", "product": "TurboWidget"}
  - Text to analyze: ..."

## 6. Prefill the Model's Response

Claude models can sometimes be "chatty," adding conversational filler before getting to the point (e.g., "Certainly, here is the summary you requested..."). To get a direct, clean output, you can use the Assistant turn to provide the very beginning of the expected response. This forces the model to continue directly from your provided text.
- **User Prompt:** ...Please provide the summary as a bulleted list.
- **Assistant Prefill:** *
By prefilling the first bullet point, you ensure the model's response begins immediately with the list, adhering strictly to the requested format.

By combining these core techniques, a prompt engineer transforms a simple request into a robust, structured, and context-rich briefing that enables the AI to function as a reliable and highly specialized tool.

