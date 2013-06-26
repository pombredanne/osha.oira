from htmllaundry.cleaners import LaundryCleaner


HomepageCleaner = LaundryCleaner(
    page_structure=False,
    remove_unknown_tags=False,
    allow_tags=['blockquote', 'a', 'img', 'em', 'p', 'strong',
                'h3', 'h4', 'h5', 'ul', 'ol', 'li', 'sub', 'sup',
                'abbr', 'acronym', 'dl', 'dt', 'dd', 'cite',
                'dft', 'br', 'table', 'tr', 'td', 'th', 'thead',
                'tbody', 'tfoot'],
    safe_attrs_only=True,
    add_nofollow=True,
    scripts=True,
    javascript=True,
    comments=False,
    style=True,
    links=False,
    meta=False,
    processing_instructions=False,
    frames=False,
    annoying_tags=False
)
