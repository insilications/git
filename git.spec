#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : git
Version  : 2.6.2
Release  : 50
URL      : https://www.kernel.org/pub/software/scm/git/git-2.6.2.tar.gz
Source0  : https://www.kernel.org/pub/software/scm/git/git-2.6.2.tar.gz
Summary  : Core git tools
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSL-1.0 GPL-2.0
Requires: git-bin
Requires: git-data
Requires: git-locales
Requires: git-doc
BuildRequires : asciidoc
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : perl-Error
BuildRequires : tcl
BuildRequires : tk
BuildRequires : zlib-dev

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs the core tools with minimal dependencies.  To
install all git packages, including tools for integrating with other
SCMs, install the git-all meta-package.

%package bin
Summary: bin components for the git package.
Group: Binaries
Requires: git-data

%description bin
bin components for the git package.


%package data
Summary: data components for the git package.
Group: Data

%description data
data components for the git package.


%package doc
Summary: doc components for the git package.
Group: Documentation

%description doc
doc components for the git package.


%package locales
Summary: locales components for the git package.
Group: Default

%description locales
locales components for the git package.


%prep
%setup -q -n git-2.6.2

%build
%configure --disable-static --with-expat --with-libpcre
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
rm -rf %{buildroot}
%make_install
%find_lang git

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Git.pm
/usr/lib/perl5/site_perl/5.22.0/Git/I18N.pm
/usr/lib/perl5/site_perl/5.22.0/Git/IndexInfo.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Editor.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Fetcher.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/GlobSpec.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Log.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Memoize/YAML.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Migration.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Prompt.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Ra.pm
/usr/lib/perl5/site_perl/5.22.0/Git/SVN/Utils.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/Git/.packlist

%files bin
%defattr(-,root,root,-)
/usr/bin/git
/usr/bin/git-cvsserver
/usr/bin/git-receive-pack
/usr/bin/git-shell
/usr/bin/git-upload-archive
/usr/bin/git-upload-pack
/usr/bin/gitk
/usr/libexec/git-core/git
/usr/libexec/git-core/git-add
/usr/libexec/git-core/git-add--interactive
/usr/libexec/git-core/git-am
/usr/libexec/git-core/git-annotate
/usr/libexec/git-core/git-apply
/usr/libexec/git-core/git-archimport
/usr/libexec/git-core/git-archive
/usr/libexec/git-core/git-bisect
/usr/libexec/git-core/git-bisect--helper
/usr/libexec/git-core/git-blame
/usr/libexec/git-core/git-branch
/usr/libexec/git-core/git-bundle
/usr/libexec/git-core/git-cat-file
/usr/libexec/git-core/git-check-attr
/usr/libexec/git-core/git-check-ignore
/usr/libexec/git-core/git-check-mailmap
/usr/libexec/git-core/git-check-ref-format
/usr/libexec/git-core/git-checkout
/usr/libexec/git-core/git-checkout-index
/usr/libexec/git-core/git-cherry
/usr/libexec/git-core/git-cherry-pick
/usr/libexec/git-core/git-citool
/usr/libexec/git-core/git-clean
/usr/libexec/git-core/git-clone
/usr/libexec/git-core/git-column
/usr/libexec/git-core/git-commit
/usr/libexec/git-core/git-commit-tree
/usr/libexec/git-core/git-config
/usr/libexec/git-core/git-count-objects
/usr/libexec/git-core/git-credential
/usr/libexec/git-core/git-credential-cache
/usr/libexec/git-core/git-credential-cache--daemon
/usr/libexec/git-core/git-credential-store
/usr/libexec/git-core/git-cvsexportcommit
/usr/libexec/git-core/git-cvsimport
/usr/libexec/git-core/git-cvsserver
/usr/libexec/git-core/git-daemon
/usr/libexec/git-core/git-describe
/usr/libexec/git-core/git-diff
/usr/libexec/git-core/git-diff-files
/usr/libexec/git-core/git-diff-index
/usr/libexec/git-core/git-diff-tree
/usr/libexec/git-core/git-difftool
/usr/libexec/git-core/git-difftool--helper
/usr/libexec/git-core/git-fast-export
/usr/libexec/git-core/git-fast-import
/usr/libexec/git-core/git-fetch
/usr/libexec/git-core/git-fetch-pack
/usr/libexec/git-core/git-filter-branch
/usr/libexec/git-core/git-fmt-merge-msg
/usr/libexec/git-core/git-for-each-ref
/usr/libexec/git-core/git-format-patch
/usr/libexec/git-core/git-fsck
/usr/libexec/git-core/git-fsck-objects
/usr/libexec/git-core/git-gc
/usr/libexec/git-core/git-get-tar-commit-id
/usr/libexec/git-core/git-grep
/usr/libexec/git-core/git-gui
/usr/libexec/git-core/git-gui--askpass
/usr/libexec/git-core/git-hash-object
/usr/libexec/git-core/git-help
/usr/libexec/git-core/git-http-backend
/usr/libexec/git-core/git-http-fetch
/usr/libexec/git-core/git-http-push
/usr/libexec/git-core/git-imap-send
/usr/libexec/git-core/git-index-pack
/usr/libexec/git-core/git-init
/usr/libexec/git-core/git-init-db
/usr/libexec/git-core/git-instaweb
/usr/libexec/git-core/git-interpret-trailers
/usr/libexec/git-core/git-log
/usr/libexec/git-core/git-ls-files
/usr/libexec/git-core/git-ls-remote
/usr/libexec/git-core/git-ls-tree
/usr/libexec/git-core/git-mailinfo
/usr/libexec/git-core/git-mailsplit
/usr/libexec/git-core/git-merge
/usr/libexec/git-core/git-merge-base
/usr/libexec/git-core/git-merge-file
/usr/libexec/git-core/git-merge-index
/usr/libexec/git-core/git-merge-octopus
/usr/libexec/git-core/git-merge-one-file
/usr/libexec/git-core/git-merge-ours
/usr/libexec/git-core/git-merge-recursive
/usr/libexec/git-core/git-merge-resolve
/usr/libexec/git-core/git-merge-subtree
/usr/libexec/git-core/git-merge-tree
/usr/libexec/git-core/git-mergetool
/usr/libexec/git-core/git-mergetool--lib
/usr/libexec/git-core/git-mktag
/usr/libexec/git-core/git-mktree
/usr/libexec/git-core/git-mv
/usr/libexec/git-core/git-name-rev
/usr/libexec/git-core/git-notes
/usr/libexec/git-core/git-p4
/usr/libexec/git-core/git-pack-objects
/usr/libexec/git-core/git-pack-redundant
/usr/libexec/git-core/git-pack-refs
/usr/libexec/git-core/git-parse-remote
/usr/libexec/git-core/git-patch-id
/usr/libexec/git-core/git-prune
/usr/libexec/git-core/git-prune-packed
/usr/libexec/git-core/git-pull
/usr/libexec/git-core/git-push
/usr/libexec/git-core/git-quiltimport
/usr/libexec/git-core/git-read-tree
/usr/libexec/git-core/git-rebase
/usr/libexec/git-core/git-rebase--am
/usr/libexec/git-core/git-rebase--interactive
/usr/libexec/git-core/git-rebase--merge
/usr/libexec/git-core/git-receive-pack
/usr/libexec/git-core/git-reflog
/usr/libexec/git-core/git-relink
/usr/libexec/git-core/git-remote
/usr/libexec/git-core/git-remote-ext
/usr/libexec/git-core/git-remote-fd
/usr/libexec/git-core/git-remote-ftp
/usr/libexec/git-core/git-remote-ftps
/usr/libexec/git-core/git-remote-http
/usr/libexec/git-core/git-remote-https
/usr/libexec/git-core/git-remote-testsvn
/usr/libexec/git-core/git-repack
/usr/libexec/git-core/git-replace
/usr/libexec/git-core/git-request-pull
/usr/libexec/git-core/git-rerere
/usr/libexec/git-core/git-reset
/usr/libexec/git-core/git-rev-list
/usr/libexec/git-core/git-rev-parse
/usr/libexec/git-core/git-revert
/usr/libexec/git-core/git-rm
/usr/libexec/git-core/git-send-email
/usr/libexec/git-core/git-send-pack
/usr/libexec/git-core/git-sh-i18n
/usr/libexec/git-core/git-sh-i18n--envsubst
/usr/libexec/git-core/git-sh-setup
/usr/libexec/git-core/git-shell
/usr/libexec/git-core/git-shortlog
/usr/libexec/git-core/git-show
/usr/libexec/git-core/git-show-branch
/usr/libexec/git-core/git-show-index
/usr/libexec/git-core/git-show-ref
/usr/libexec/git-core/git-stage
/usr/libexec/git-core/git-stash
/usr/libexec/git-core/git-status
/usr/libexec/git-core/git-stripspace
/usr/libexec/git-core/git-submodule
/usr/libexec/git-core/git-svn
/usr/libexec/git-core/git-symbolic-ref
/usr/libexec/git-core/git-tag
/usr/libexec/git-core/git-unpack-file
/usr/libexec/git-core/git-unpack-objects
/usr/libexec/git-core/git-update-index
/usr/libexec/git-core/git-update-ref
/usr/libexec/git-core/git-update-server-info
/usr/libexec/git-core/git-upload-archive
/usr/libexec/git-core/git-upload-pack
/usr/libexec/git-core/git-var
/usr/libexec/git-core/git-verify-commit
/usr/libexec/git-core/git-verify-pack
/usr/libexec/git-core/git-verify-tag
/usr/libexec/git-core/git-web--browse
/usr/libexec/git-core/git-whatchanged
/usr/libexec/git-core/git-worktree
/usr/libexec/git-core/git-write-tree
/usr/libexec/git-core/mergetools/araxis
/usr/libexec/git-core/mergetools/bc
/usr/libexec/git-core/mergetools/bc3
/usr/libexec/git-core/mergetools/codecompare
/usr/libexec/git-core/mergetools/deltawalker
/usr/libexec/git-core/mergetools/diffmerge
/usr/libexec/git-core/mergetools/diffuse
/usr/libexec/git-core/mergetools/ecmerge
/usr/libexec/git-core/mergetools/emerge
/usr/libexec/git-core/mergetools/gvimdiff
/usr/libexec/git-core/mergetools/gvimdiff2
/usr/libexec/git-core/mergetools/gvimdiff3
/usr/libexec/git-core/mergetools/kdiff3
/usr/libexec/git-core/mergetools/kompare
/usr/libexec/git-core/mergetools/meld
/usr/libexec/git-core/mergetools/opendiff
/usr/libexec/git-core/mergetools/p4merge
/usr/libexec/git-core/mergetools/tkdiff
/usr/libexec/git-core/mergetools/tortoisemerge
/usr/libexec/git-core/mergetools/vimdiff
/usr/libexec/git-core/mergetools/vimdiff2
/usr/libexec/git-core/mergetools/vimdiff3
/usr/libexec/git-core/mergetools/winmerge
/usr/libexec/git-core/mergetools/xxdiff

%files data
%defattr(-,root,root,-)
/usr/share/git-core/templates/description
/usr/share/git-core/templates/hooks/applypatch-msg.sample
/usr/share/git-core/templates/hooks/commit-msg.sample
/usr/share/git-core/templates/hooks/post-update.sample
/usr/share/git-core/templates/hooks/pre-applypatch.sample
/usr/share/git-core/templates/hooks/pre-commit.sample
/usr/share/git-core/templates/hooks/pre-push.sample
/usr/share/git-core/templates/hooks/pre-rebase.sample
/usr/share/git-core/templates/hooks/prepare-commit-msg.sample
/usr/share/git-core/templates/hooks/update.sample
/usr/share/git-core/templates/info/exclude
/usr/share/git-gui/lib/about.tcl
/usr/share/git-gui/lib/blame.tcl
/usr/share/git-gui/lib/branch.tcl
/usr/share/git-gui/lib/branch_checkout.tcl
/usr/share/git-gui/lib/branch_create.tcl
/usr/share/git-gui/lib/branch_delete.tcl
/usr/share/git-gui/lib/branch_rename.tcl
/usr/share/git-gui/lib/browser.tcl
/usr/share/git-gui/lib/checkout_op.tcl
/usr/share/git-gui/lib/choose_font.tcl
/usr/share/git-gui/lib/choose_repository.tcl
/usr/share/git-gui/lib/choose_rev.tcl
/usr/share/git-gui/lib/class.tcl
/usr/share/git-gui/lib/commit.tcl
/usr/share/git-gui/lib/console.tcl
/usr/share/git-gui/lib/database.tcl
/usr/share/git-gui/lib/date.tcl
/usr/share/git-gui/lib/diff.tcl
/usr/share/git-gui/lib/encoding.tcl
/usr/share/git-gui/lib/error.tcl
/usr/share/git-gui/lib/git-gui.ico
/usr/share/git-gui/lib/index.tcl
/usr/share/git-gui/lib/line.tcl
/usr/share/git-gui/lib/logo.tcl
/usr/share/git-gui/lib/merge.tcl
/usr/share/git-gui/lib/mergetool.tcl
/usr/share/git-gui/lib/msgs/bg.msg
/usr/share/git-gui/lib/msgs/de.msg
/usr/share/git-gui/lib/msgs/el.msg
/usr/share/git-gui/lib/msgs/fr.msg
/usr/share/git-gui/lib/msgs/hu.msg
/usr/share/git-gui/lib/msgs/it.msg
/usr/share/git-gui/lib/msgs/ja.msg
/usr/share/git-gui/lib/msgs/nb.msg
/usr/share/git-gui/lib/msgs/pt_br.msg
/usr/share/git-gui/lib/msgs/ru.msg
/usr/share/git-gui/lib/msgs/sv.msg
/usr/share/git-gui/lib/msgs/vi.msg
/usr/share/git-gui/lib/msgs/zh_cn.msg
/usr/share/git-gui/lib/option.tcl
/usr/share/git-gui/lib/remote.tcl
/usr/share/git-gui/lib/remote_add.tcl
/usr/share/git-gui/lib/remote_branch_delete.tcl
/usr/share/git-gui/lib/search.tcl
/usr/share/git-gui/lib/shortcut.tcl
/usr/share/git-gui/lib/spellcheck.tcl
/usr/share/git-gui/lib/sshkey.tcl
/usr/share/git-gui/lib/status_bar.tcl
/usr/share/git-gui/lib/tclIndex
/usr/share/git-gui/lib/themed.tcl
/usr/share/git-gui/lib/tools.tcl
/usr/share/git-gui/lib/tools_dlg.tcl
/usr/share/git-gui/lib/transport.tcl
/usr/share/git-gui/lib/win32.tcl
/usr/share/git-gui/lib/win32_shortcut.js
/usr/share/gitk/lib/msgs/bg.msg
/usr/share/gitk/lib/msgs/ca.msg
/usr/share/gitk/lib/msgs/de.msg
/usr/share/gitk/lib/msgs/es.msg
/usr/share/gitk/lib/msgs/fr.msg
/usr/share/gitk/lib/msgs/hu.msg
/usr/share/gitk/lib/msgs/it.msg
/usr/share/gitk/lib/msgs/ja.msg
/usr/share/gitk/lib/msgs/pt_br.msg
/usr/share/gitk/lib/msgs/ru.msg
/usr/share/gitk/lib/msgs/sv.msg
/usr/share/gitk/lib/msgs/vi.msg
/usr/share/gitweb/gitweb.cgi
/usr/share/gitweb/static/git-favicon.png
/usr/share/gitweb/static/git-logo.png
/usr/share/gitweb/static/gitweb.css
/usr/share/gitweb/static/gitweb.js

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files locales -f git.lang 
%defattr(-,root,root,-)

