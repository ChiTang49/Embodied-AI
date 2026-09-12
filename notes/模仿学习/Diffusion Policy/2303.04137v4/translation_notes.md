# Translation and layout notes

## Processing status

- Source: user-provided selectable-text PDF 2303.04137v4.pdf.
- PDF has 16 pages. Pages 1–11 contain title, main text, figures, tables, conclusion and the start of references; pages 12–13 are references; pages 14–16 are appendix and hardware details.
- Main prose, equations, captions, tables and appendix paragraphs were extracted with Poppler text extraction and visually checked against rendered page previews.
- paper.md is a bilingual reader rather than a Chinese-only summary. Each substantive reading block has a stable anchor (Sxxx, Fxxx, or Txxx) and a page pointer.

## Figure/table crops

- 13 figures and 7 tables were cropped from 120 dpi page renders and stored under assets/.
- Crop boxes are recorded in source_map.json in rendered-pixel coordinates.
- Crops intentionally omit surrounding body text and keep captions in Markdown so the visual object and caption remain attached semantically.
- The PDF contains many embedded image fragments because the figures are composed in LaTeX; page-render crops were therefore used for reliable semantic grouping.
- Crops are suitable for reading and citation, not pixel-perfect reconstruction of the original PDF.

## Translation conventions

- Technical names and model names remain in English when a stable Chinese equivalent would be ambiguous: Diffusion Policy, DDPM, DDIM, FiLM, Transformer, ResNet-18, LSTM-GMM, IBC, BET.
- receding-horizon control is translated as 滚动时域控制; score function as 得分函数; position control as 位置控制.
- Symbols, equation numbering, citations, units, Hz, DoF, IoU and percentage values are preserved.
- Push-T, Mug Flipping, Sauce Pouring, Periodic Spreading, BlockPush and Franka Kitchen are retained as task names with Chinese context.

## Reference section

- The references on pages 11–14 are bibliographic entries. The reader preserves their role and representative citation mapping but does not retranslate every bibliographic line, so author/title/venue formatting stays traceable to the source PDF.

## Known limitations

- The source PDF has malformed-number warnings in a few embedded objects; these affect Poppler diagnostics but not the visually inspected page renders.
- Some table and plot labels use embedded fonts with poor text extraction. Their visual content is preserved in image crops and described in the corresponding table/figure cards.
- The source does not include supplementary videos. Mentions of videos are retained as claims about the supplement, but no video asset is included.
