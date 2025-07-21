# BNU Thesis Template - Maintenance Guide

## Project Overview

This is a comprehensive LaTeX thesis template for Beijing Normal University (BNU) that supports bachelor's, master's, and doctoral thesis formats. The template has been approved by the university library and meets all current formatting requirements.

## Project Structure

### Core LaTeX Files

#### Main Document Files
- `main.tex` - Main document file with compilation instructions and document structure
- `bnuthesis.cls` - Main class file (1188 lines) defining thesis structure and formatting
- `bnuthesis.cfg` - Configuration file with Chinese text and formatting settings
- `bnutils.sty` - Utility package with common commands and packages
- `bnubib.bst` - Bibliography style file for BNU format

#### Bibliography and References
- `gbt7714.sty` - Chinese bibliography package
- `gbt7714-numerical.bst` - Bibliography style for GB/T 7714-2015 standard
- `ref/refs.bib` - Bibliography database with example entries

### Content Organization

#### Data Directory (`data/`)
- `cover.tex` - Thesis cover page and abstract definitions
- `chap1.tex` - First chapter with comprehensive examples (485 lines)
- `chap2.tex` - Second chapter (74 lines)
- `appendix.tex` - Appendix content (224 lines)
- `ack.tex` - Acknowledgments (12 lines)
- `paper.tex` - Academic achievements section (15 lines)

#### Assets
- `figures/` - Image files including BNU logos (black/red versions)
- `fonts/` - Chinese font files (SimSun, SimHei, SimKai, SimLi, SimYou)

#### Documentation
- `others/` - PDF documentation and university guidelines
- `README.md` - Project overview and basic instructions

## Technical Specifications

### Compilation Requirements
- **Engine**: XeLaTeX (required for Chinese character support)
- **TeX Distribution**: TeX Live 2021 or 2022
- **Encoding**: UTF-8
- **Paper Size**: A4
- **Font Size**: 12pt

### Supported Degree Types
1. **Bachelor's Thesis** (`bachelor` option)
   - Undergraduate thesis format
   - Black BNU logo
   - Simplified chapter numbering

2. **Master's Thesis** (`master` option)
   - Graduate thesis format
   - Red BNU logo
   - Full chapter numbering (第 X 章)

3. **Doctoral Thesis** (`doctor` option)
   - PhD thesis format
   - Red BNU logo
   - Full chapter numbering
   - Additional requirements for book spine

### Key Features

#### Chinese Language Support
- Full UTF-8 encoding support
- Multiple Chinese font families (SimSun, SimHei, SimKai, SimLi, SimYou)
- Proper character spacing and line breaking
- Chinese bibliography formatting

#### Bibliography System
- GB/T 7714-2015 standard compliance
- Support for both numerical and author-year citation styles
- Automatic bibliography generation
- Chinese and English reference support

#### Document Structure
- Front matter (cover, abstract, table of contents)
- Main matter (chapters)
- Back matter (bibliography, appendix, acknowledgments)
- Proper page numbering and headers

#### Advanced Formatting
- Professional table formatting with booktabs
- Figure and table captions
- Mathematical equation support
- Cross-referencing system
- Footnote support

## Maintenance Procedures

### Adding New Content

#### Adding a New Chapter
1. Create a new `.tex` file in the `data/` directory
2. Use the chapter template from `chap1.tex`
3. Add `\include{data/filename}` to `main.tex`
4. Update table of contents automatically

#### Modifying Cover Information
1. Edit `data/cover.tex`
2. Update thesis title, author, supervisor information
3. Modify abstract content
4. Update keywords

#### Adding References
1. Add entries to `ref/refs.bib`
2. Use `\cite{key}` in your text
3. Bibliography will be generated automatically

### Style Customization

#### Modifying Class Options
Edit `main.tex` line 10:
```latex
\documentclass[master]{bnuthesis}
% Options: bachelor, master, doctor
```

#### Changing Fonts
Modify `bnuthesis.cls` font definitions:
- Chinese fonts: SimSun, SimHei, SimKai, SimLi, SimYou
- English fonts: Times New Roman, Arial

#### Adjusting Page Layout
Edit `bnuthesis.cls`:
- Page margins
- Header/footer style
- Chapter title formatting
- Section numbering

### Troubleshooting

#### Common Compilation Issues
1. **XeLaTeX Required**: Ensure using XeLaTeX engine
2. **Font Issues**: Check font installation in `fonts/` directory
3. **Encoding Problems**: Verify UTF-8 encoding in all files
4. **Bibliography Errors**: Check `.bib` file syntax

#### Performance Optimization
1. Use `\include` instead of `\input` for large files
2. Optimize image sizes in `figures/` directory
3. Minimize font usage to reduce compilation time

## Development Guidelines

### Code Standards
- Use UTF-8 encoding for all files
- Follow LaTeX best practices
- Add comments for complex sections
- Maintain consistent indentation

### Version Control
- Track changes in core files (`bnuthesis.cls`, `main.tex`)
- Document major updates in commit messages
- Test compilation after each change
- Maintain backup of working versions

### Testing Procedures
1. Test compilation with all degree types
2. Verify Chinese character rendering
3. Check bibliography generation
4. Validate table and figure formatting
5. Test cross-references

## Future Enhancements

### Planned Features
1. **Book Spine Support**: Add support for doctoral thesis book spine
2. **Enhanced Bibliography**: Improve citation style options
3. **Template Variants**: Create specialized templates for different departments
4. **Online Integration**: Better Overleaf compatibility

### Known Issues
1. Doctoral thesis book spine not implemented
2. Some advanced bibliography features pending
3. Limited template customization options
4. Font installation complexity for new users

## Support and Resources

### Documentation
- University guidelines in `others/` directory
- Example content in `data/` files
- Bibliography examples in `ref/refs.bib`

### External Resources
- Overleaf template: [BNU Thesis Template](https://www.overleaf.com/latex/templates/bnu-bachelor-slash-master-slash-phd-thesis-template/nhvczzkqtrqq)
- LaTeX learning resources from BNU Astronomy Department
- GB/T 7714-2015 bibliography standard documentation

### Contact Information
- Template maintainer: [Contact information needed]
- University library: [Contact information needed]
- Technical support: [Contact information needed]

---

*Last updated: [Current Date]*
*Template version: 1.52*
*Compatible with: TeX Live 2021/2022, XeLaTeX* 