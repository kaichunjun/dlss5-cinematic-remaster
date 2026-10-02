# Generative-route evidence and limits

This package reuses the original-based v3 generative workflow. The split on 2026-10-01 changes packaging and invocation, not the image model. **No new generation was performed for this split.** Historical prompts and assessments are retained in [v3-test-prompts.json](v3-test-prompts.json) and [v3-test-results.json](v3-test-results.json).

| Historical case | Existing result | Limit |
|---|---|---|
| Rain-night anime portrait / Normal | Assistant assessment `passed-on-this-image`; stronger existing lantern-side illumination | Minute drawn-line variations; user approval pending |
| Eight-character ensemble plus two distant figures / Deep | `qualified-preview`; visible existing parchment/material light shaping | Fine ornament redraw, stronger local color, reduced result resolution; user approval pending |

Two historical executions on two inputs, not universal reliability or a deterministic benchmark. They were made with the built-in image editor; model version, seed, denoise and protected masks were not exposed. Prompt text is a goal, never a pixel lock. An earlier maximum-strength world-building attempt added scene content and failed fidelity; excessive saturation also received negative feedback. Preserve these failure lessons by checking content separately from atmosphere.

Photos, exact text/logo preservation, batch consistency and video are unvalidated here. A static comparison cannot prove temporal consistency. Root-repository runtime notes are separate community-app history; this Skill does not invoke DLSS or render a desktop/game in real time.
