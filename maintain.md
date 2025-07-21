# BNU Thesis Template - Maintenance Guide

## Project Overview

This is a comprehensive LaTeX thesis template for Beijing Normal University (BNU) that supports bachelor's, master's, and doctoral thesis formats. The template has been approved by the university library and meets all current formatting requirements.

## Recent Updates and Improvements

### 🆕 Latest Features (2024)
- **Custom Footnote Citations**: Enhanced `\footcite` command that displays full bibliographic information in footnotes
- **Automated Compilation Script**: `run.bat` for Windows users to automate the full compilation process
- **Missing Reference Checker**: Python script (`check_all_missing_refs.py`) to identify missing citation keys in bibliography
- **Continuous Footnote Numbering**: Fixed footnote numbering to be continuous across the document
- **Vietnamese Language Support**: Added support for Vietnamese text with proper font handling

### 🔧 Technical Improvements
- **Bibliography Integration**: Full integration with `refs.bib` for comprehensive citation management
- **Compilation Automation**: One-click compilation with automatic PDF opening
- **Error Detection**: Tools to identify and fix missing bibliography entries
- **Cross-Platform Support**: Enhanced compatibility across different operating systems

## Recent Updates and Improvements

### 🆕 Latest Features (2024)
- **Custom Footnote Citations**: Enhanced `\footcite` command that displays full bibliographic information in footnotes
- **Automated Compilation Script**: `run.bat` for Windows users to automate the full compilation process
- **Missing Reference Checker**: Python script (`check_all_missing_refs.py`) to identify missing citation keys in bibliography
- **Continuous Footnote Numbering**: Fixed footnote numbering to be continuous across the document
- **Vietnamese Language Support**: Added support for Vietnamese text with proper font handling

### 🔧 Technical Improvements
- **Bibliography Integration**: Full integration with `refs.bib` for comprehensive citation management
- **Compilation Automation**: One-click compilation with automatic PDF opening
- **Error Detection**: Tools to identify and fix missing bibliography entries
- **Cross-Platform Support**: Enhanced compatibility across different operating systems

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

#### Documentation and Tools
- `others/` - PDF documentation and university guidelines
- `README.md` - Project overview and basic instructions
- `run.bat` - Automated compilation script for Windows
- `check_all_missing_refs.py` - Python script to check missing references

### Content Organization

#### Data Directory (`data/`)
- `cover.tex` - Thesis cover page and abstract definitions
- `chap1.tex` - First chapter with comprehensive examples (530 lines)
- `chap2.tex` - Second chapter (74 lines)
- `appendix.tex` - Appendix content (224 lines)
- `ack.tex` - Acknowledgments (12 lines)
- `paper.tex` - Academic achievements section (15 lines)

#### Assets
- `figures/` - Image files including BNU logos (black/red versions)
- `fonts/` - Chinese font files (SimSun, SimHei, SimKai, SimLi, SimYou)
- `image/` - Additional image files for thesis content

#### Documentation and Tools
- `others/` - PDF documentation and university guidelines
- `README.md` - Project overview and basic instructions
- `run.bat` - Automated compilation script for Windows
- `check_all_missing_refs.py` - Python script to check missing references

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

#### Vietnamese Language Support
- Added font support for Vietnamese text
- Proper handling of Vietnamese characters
- Integration with existing Chinese font system

#### Enhanced Bibliography System
- GB/T 7714-2015 standard compliance
- Support for both numerical and author-year citation styles
- Automatic bibliography generation
- Chinese and English reference support
- Custom `\footcite` command for full bibliography in footnotes

#### Vietnamese Language Support
- Added font support for Vietnamese text
- Proper handling of Vietnamese characters
- Integration with existing Chinese font system

#### Enhanced Bibliography System
- GB/T 7714-2015 standard compliance
- Support for both numerical and author-year citation styles
- Automatic bibliography generation
- Chinese and English reference support
- Custom `\footcite` command for full bibliography in footnotes

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
- Enhanced footnote support with continuous numbering

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
2. Use `\cite{key}` for regular citations
3. Use `\footcite{key}` for footnote citations with full bibliography info
4. Use `\footcitewith{key}{text}` for footnote citations with additional text
5. Bibliography will be generated automatically

### Using the New Tools

#### Automated Compilation (Windows)
1. Run `run.bat` from command line
2. Script will automatically:
   - Clean auxiliary files
   - Run full compilation sequence (xelatex → bibtex → xelatex → xelatex)
   - Open PDF when complete

#### Checking Missing References
1. Run `python check_all_missing_refs.py`
2. Script will:
   - Scan all `.tex` files in project
   - Compare with `refs.bib` file
   - List missing citation keys
   - Help identify empty bibliography entries

### Style Customization

#### Modifying Class Options
Edit `main.tex` line 10:
```latex
\documentclass[doctor]{bnuthesis}
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
5. **Empty Bibliography Entries**: Use `check_all_missing_refs.py` to identify missing keys
5. **Empty Bibliography Entries**: Use `check_all_missing_refs.py` to identify missing keys

#### Performance Optimization
1. Use `\include` instead of `\input` for large files
2. Optimize image sizes in `figures/` directory
3. Minimize font usage to reduce compilation time
4. Use automated compilation script for consistent results
4. Use automated compilation script for consistent results

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
6. Verify footnote functionality
7. Test automated compilation script
8. Run missing reference checker
6. Verify footnote functionality
7. Test automated compilation script
8. Run missing reference checker

## Future Enhancements

### Planned Features
1. **Book Spine Support**: Add support for doctoral thesis book spine
2. **Enhanced Bibliography**: Improve citation style options
3. **Template Variants**: Create specialized templates for different departments
4. **Online Integration**: Better Overleaf compatibility
5. **Additional Language Support**: Support for more languages
6. **Advanced Citation Tools**: More sophisticated citation management
5. **Additional Language Support**: Support for more languages
6. **Advanced Citation Tools**: More sophisticated citation management

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
- Updated README with latest features
- Updated README with latest features

### External Resources
- Overleaf template: [BNU Thesis Template](https://www.overleaf.com/latex/templates/bnu-bachelor-slash-master-slash-phd-thesis-template/nhvczzkqtrqq)
- LaTeX learning resources from BNU Astronomy Department
- GB/T 7714-2015 bibliography standard documentation

### Contact Information
- Template maintainer: [Contact information needed]
- University library: [Contact information needed]
- Technical support: [Contact information needed]

---

*Last updated: December 2024*
*Template version: 1.53*
*Compatible with: TeX Live 2021/2022, XeLaTeX* 