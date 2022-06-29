import tokenize

from .. import settings
from ..misc import PylintOdooTokenChecker

ODOO_MSGS = {
    # C->convention R->refactor W->warning E->error F->fatal
    "W%d02"
    % settings.BASE_FORMAT_ID: (
        "Use of vim comment",
        "use-vim-comment",
        settings.DESC_DFLT,
    ),
}


class FormatChecker(PylintOdooTokenChecker):

    name = settings.CFG_SECTION
    msgs = ODOO_MSGS

    def process_tokens(self, tokens):
        if self.linter.is_message_enabled("use-vim-comment"):
            for idx, (
                tok_type,
                token_content,
                start_line_col,
                end_line_col,
                line_content,
            ) in enumerate(tokens):
                if tokenize.COMMENT == tok_type and token_content.strip(
                    "# "
                ).lower().startswith("vim:"):
                    self.add_message("use-vim-comment", line=start_line_col[0])
