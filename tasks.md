# Goals of the re-design

1. Organize the existing documentation in 4 main sections: Access, Compute,
   Cloud and Data
2. All documents should be visible and reachable organically through
   navigation. Users should be able to figure out were to find information
   without search.
3. Site-specific information should be minimized. Disagreements between sites
   will be forwarded to a CUE meeting. Remaining site-specific information will
   be organized in tabs to avoid clutter.

## Main Tasks

1. Phase 1
   * ️ configure PyData theme
   * ️✅ define color scheme
   * ✅ adapt documentation to Sphinx_Design formatting elements
   * ✅ organize documentation in 4 main sections
   * ✅ fix all formatting errors from RST files
   * ✅ add all RST files to a TOC tree
   * ✅ disable automatic labels from section names
2. Phase 2
   * ✅ re-structure separation between OS with cards
   * ✅ review mixed use of TOCs and sections
   * ✅ review sections with large differences between sites: VNC, VPN
   * ✅ seek outdated information in documentation
   * ✅ add custom 404 page
3. Phase 3
   * ✅ split _Access and data transfer_ in 2 different sections
   * ✅ reorganize _Accounts and access_ info to make SSH keys optional
   * ✅ merge all information about data and storage in a single section
   * ✅ replace images with figures
   * ✅ fix broken links with redirects (sphinx-reredirects)
   * ✅ write style guide
   * ✅ make CI fail on any Sphinx warning
4. Phase 4
   * 🔄 add support for markdown with MyST
   * ⬜ add widget to preselect home institute

