/**
 * Translates all text in the active Google Slides presentation to Korean.
 * Run this function from the Apps Script editor.
 *
 * Note: Inline character formatting (e.g., bold/italic on specific words)
 * will be reset to the paragraph's default style after translation.
 * Paragraph-level styles (font size, alignment, color) are preserved.
 */
function translatePresentationToKorean() {
  var presentation = SlidesApp.getActivePresentation();
  var slides = presentation.getSlides();

  for (var i = 0; i < slides.length; i++) {
    var pageElements = slides[i].getPageElements();
    for (var j = 0; j < pageElements.length; j++) {
      translateElement(pageElements[j]);
    }
  }

  Logger.log('Translation to Korean complete!');
}

/**
 * Dispatches translation based on element type.
 * Handles shapes, tables, and groups recursively.
 */
function translateElement(element) {
  switch (element.getPageElementType()) {
    case SlidesApp.PageElementType.SHAPE:
      translateTextRange(element.asShape().getText());
      break;

    case SlidesApp.PageElementType.TABLE:
      var table = element.asTable();
      for (var r = 0; r < table.getNumRows(); r++) {
        for (var c = 0; c < table.getNumColumns(); c++) {
          translateTextRange(table.getCell(r, c).getText());
        }
      }
      break;

    case SlidesApp.PageElementType.GROUP:
      var children = element.asGroup().getChildren();
      for (var k = 0; k < children.length; k++) {
        translateElement(children[k]);
      }
      break;

    default:
      // WordArt, images, videos, etc. — no text to translate
      break;
  }
}

/**
 * Translates a TextRange to Korean, paragraph by paragraph.
 * Translating paragraph by paragraph preserves paragraph-level styling
 * (alignment, spacing, font size) better than replacing the full block.
 */
function translateTextRange(textRange) {
  var paragraphs = textRange.getParagraphs();

  for (var i = 0; i < paragraphs.length; i++) {
    var para = paragraphs[i];
    var originalText = para.getRange().asString();

    // Skip empty paragraphs or whitespace-only content
    if (originalText.trim().length === 0) continue;

    // Strip the trailing newline that Slides appends to each paragraph
    // before translating, then restore it when setting text.
    var textToTranslate = originalText.replace(/\n$/, '');
    if (textToTranslate.length === 0) continue;

    try {
      var translated = LanguageApp.translate(textToTranslate, '', 'ko');
      para.getRange().setText(translated);
    } catch (e) {
      Logger.log('Failed to translate paragraph ' + i + ': ' + e.message);
    }
  }
}
