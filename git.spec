#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : git
Version  : 2.21.0
Release  : 146
URL      : https://www.kernel.org/pub/software/scm/git/git-2.21.0.tar.xz
Source0  : https://www.kernel.org/pub/software/scm/git/git-2.21.0.tar.xz
Summary  : the fast distributed version control system
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSL-1.0 GPL-2.0 MIT
Requires: git-bin = %{version}-%{release}
Requires: git-data = %{version}-%{release}
Requires: git-libexec = %{version}-%{release}
Requires: git-license = %{version}-%{release}
Requires: git-locales = %{version}-%{release}
Requires: git-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-golang
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : expat-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pcre2-dev
BuildRequires : perl-Error
BuildRequires : python3-dev
BuildRequires : tcl
BuildRequires : tk
BuildRequires : util-linux
BuildRequires : xmlto
BuildRequires : zlib-dev
Patch1: 0001-Set-default-autocorrect-timeout-to-1.5-seconds.patch
Patch2: 0002-Fix-expected-result-for-a-for-each-ref-test.patch

%description
git-jump
========
Git-jump is a script for helping you jump to "interesting" parts of your
project in your editor. It works by outputting a set of interesting
spots in the "quickfix" format, which editors like vim can use as a
queue of places to visit (this feature is usually used to jump to errors
produced by a compiler). For example, given a diff like this:

%package bin
Summary: bin components for the git package.
Group: Binaries
Requires: git-data = %{version}-%{release}
Requires: git-libexec = %{version}-%{release}
Requires: git-license = %{version}-%{release}

%description bin
bin components for the git package.


%package data
Summary: data components for the git package.
Group: Data

%description data
data components for the git package.


%package extras
Summary: extras components for the git package.
Group: Default

%description extras
extras components for the git package.


%package libexec
Summary: libexec components for the git package.
Group: Default
Requires: git-license = %{version}-%{release}

%description libexec
libexec components for the git package.


%package license
Summary: license components for the git package.
Group: Default

%description license
license components for the git package.


%package locales
Summary: locales components for the git package.
Group: Default

%description locales
locales components for the git package.


%package man
Summary: man components for the git package.
Group: Default

%description man
man components for the git package.


%prep
%setup -q -n git-2.21.0
%patch1 -p1
%patch2 -p1
pushd ..
cp -a git-2.21.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554385404
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-expat --with-libpcre --with-curl \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --with-expat --with-libpcre --with-curl \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} test

%install
export SOURCE_DATE_EPOCH=1554385404
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/git
cp COPYING %{buildroot}/usr/share/package-licenses/git/COPYING
cp compat/nedmalloc/License.txt %{buildroot}/usr/share/package-licenses/git/compat_nedmalloc_License.txt
cp contrib/persistent-https/LICENSE %{buildroot}/usr/share/package-licenses/git/contrib_persistent-https_LICENSE
cp contrib/subtree/COPYING %{buildroot}/usr/share/package-licenses/git/contrib_subtree_COPYING
cp sha1dc/LICENSE.txt %{buildroot}/usr/share/package-licenses/git/sha1dc_LICENSE.txt
cp t/diff-lib/COPYING %{buildroot}/usr/share/package-licenses/git/t_diff-lib_COPYING
cp vcs-svn/LICENSE %{buildroot}/usr/share/package-licenses/git/vcs-svn_LICENSE
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang git
## install_append content
install -D -m 00644 contrib/completion/git-completion.bash %{buildroot}/usr/share/bash-completion/completions/git
install -D -m 00644 contrib/completion/git-prompt.sh %{buildroot}/usr/share/git-core/git-prompt.sh
pushd Documentation
make %{?_smp_mflags} man
make DESTDIR=%{buildroot} install
popd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/git-cvsserver
%exclude /usr/bin/gitk
/usr/bin/git
/usr/bin/git-receive-pack
/usr/bin/git-shell
/usr/bin/git-upload-archive
/usr/bin/git-upload-pack
/usr/bin/haswell/git
/usr/bin/haswell/git-receive-pack
/usr/bin/haswell/git-shell
/usr/bin/haswell/git-upload-archive
/usr/bin/haswell/git-upload-pack

%files data
%defattr(-,root,root,-)
%exclude /usr/share/git-core/templates/hooks/fsmonitor-watchman.sample
%exclude /usr/share/git-core/templates/hooks/pre-rebase.sample
%exclude /usr/share/git-core/templates/hooks/prepare-commit-msg.sample
%exclude /usr/share/git-gui/lib/about.tcl
%exclude /usr/share/git-gui/lib/blame.tcl
%exclude /usr/share/git-gui/lib/branch.tcl
%exclude /usr/share/git-gui/lib/branch_checkout.tcl
%exclude /usr/share/git-gui/lib/branch_create.tcl
%exclude /usr/share/git-gui/lib/branch_delete.tcl
%exclude /usr/share/git-gui/lib/branch_rename.tcl
%exclude /usr/share/git-gui/lib/browser.tcl
%exclude /usr/share/git-gui/lib/checkout_op.tcl
%exclude /usr/share/git-gui/lib/choose_font.tcl
%exclude /usr/share/git-gui/lib/choose_repository.tcl
%exclude /usr/share/git-gui/lib/choose_rev.tcl
%exclude /usr/share/git-gui/lib/class.tcl
%exclude /usr/share/git-gui/lib/commit.tcl
%exclude /usr/share/git-gui/lib/console.tcl
%exclude /usr/share/git-gui/lib/database.tcl
%exclude /usr/share/git-gui/lib/date.tcl
%exclude /usr/share/git-gui/lib/diff.tcl
%exclude /usr/share/git-gui/lib/encoding.tcl
%exclude /usr/share/git-gui/lib/error.tcl
%exclude /usr/share/git-gui/lib/git-gui.ico
%exclude /usr/share/git-gui/lib/index.tcl
%exclude /usr/share/git-gui/lib/line.tcl
%exclude /usr/share/git-gui/lib/logo.tcl
%exclude /usr/share/git-gui/lib/merge.tcl
%exclude /usr/share/git-gui/lib/mergetool.tcl
%exclude /usr/share/git-gui/lib/msgs/bg.msg
%exclude /usr/share/git-gui/lib/msgs/de.msg
%exclude /usr/share/git-gui/lib/msgs/el.msg
%exclude /usr/share/git-gui/lib/msgs/fr.msg
%exclude /usr/share/git-gui/lib/msgs/hu.msg
%exclude /usr/share/git-gui/lib/msgs/it.msg
%exclude /usr/share/git-gui/lib/msgs/ja.msg
%exclude /usr/share/git-gui/lib/msgs/nb.msg
%exclude /usr/share/git-gui/lib/msgs/pt_br.msg
%exclude /usr/share/git-gui/lib/msgs/pt_pt.msg
%exclude /usr/share/git-gui/lib/msgs/ru.msg
%exclude /usr/share/git-gui/lib/msgs/sv.msg
%exclude /usr/share/git-gui/lib/msgs/vi.msg
%exclude /usr/share/git-gui/lib/msgs/zh_cn.msg
%exclude /usr/share/git-gui/lib/option.tcl
%exclude /usr/share/git-gui/lib/remote.tcl
%exclude /usr/share/git-gui/lib/remote_add.tcl
%exclude /usr/share/git-gui/lib/remote_branch_delete.tcl
%exclude /usr/share/git-gui/lib/search.tcl
%exclude /usr/share/git-gui/lib/shortcut.tcl
%exclude /usr/share/git-gui/lib/spellcheck.tcl
%exclude /usr/share/git-gui/lib/sshkey.tcl
%exclude /usr/share/git-gui/lib/status_bar.tcl
%exclude /usr/share/git-gui/lib/tclIndex
%exclude /usr/share/git-gui/lib/themed.tcl
%exclude /usr/share/git-gui/lib/tools.tcl
%exclude /usr/share/git-gui/lib/tools_dlg.tcl
%exclude /usr/share/git-gui/lib/transport.tcl
%exclude /usr/share/git-gui/lib/win32.tcl
%exclude /usr/share/git-gui/lib/win32_shortcut.js
%exclude /usr/share/gitk/lib/msgs/bg.msg
%exclude /usr/share/gitk/lib/msgs/ca.msg
%exclude /usr/share/gitk/lib/msgs/de.msg
%exclude /usr/share/gitk/lib/msgs/es.msg
%exclude /usr/share/gitk/lib/msgs/fr.msg
%exclude /usr/share/gitk/lib/msgs/hu.msg
%exclude /usr/share/gitk/lib/msgs/it.msg
%exclude /usr/share/gitk/lib/msgs/ja.msg
%exclude /usr/share/gitk/lib/msgs/pt_br.msg
%exclude /usr/share/gitk/lib/msgs/pt_pt.msg
%exclude /usr/share/gitk/lib/msgs/ru.msg
%exclude /usr/share/gitk/lib/msgs/sv.msg
%exclude /usr/share/gitk/lib/msgs/vi.msg
%exclude /usr/share/gitweb/gitweb.cgi
%exclude /usr/share/perl5/FromCPAN/Error.pm
%exclude /usr/share/perl5/FromCPAN/Mail/Address.pm
%exclude /usr/share/perl5/Git.pm
%exclude /usr/share/perl5/Git/I18N.pm
%exclude /usr/share/perl5/Git/IndexInfo.pm
%exclude /usr/share/perl5/Git/LoadCPAN.pm
%exclude /usr/share/perl5/Git/LoadCPAN/Error.pm
%exclude /usr/share/perl5/Git/LoadCPAN/Mail/Address.pm
%exclude /usr/share/perl5/Git/Packet.pm
%exclude /usr/share/perl5/Git/SVN.pm
%exclude /usr/share/perl5/Git/SVN/Editor.pm
%exclude /usr/share/perl5/Git/SVN/Fetcher.pm
%exclude /usr/share/perl5/Git/SVN/GlobSpec.pm
%exclude /usr/share/perl5/Git/SVN/Log.pm
%exclude /usr/share/perl5/Git/SVN/Memoize/YAML.pm
%exclude /usr/share/perl5/Git/SVN/Migration.pm
%exclude /usr/share/perl5/Git/SVN/Prompt.pm
%exclude /usr/share/perl5/Git/SVN/Ra.pm
%exclude /usr/share/perl5/Git/SVN/Utils.pm
/usr/share/bash-completion/completions/git
/usr/share/git-core/git-prompt.sh
/usr/share/git-core/templates/description
/usr/share/git-core/templates/hooks/applypatch-msg.sample
/usr/share/git-core/templates/hooks/commit-msg.sample
/usr/share/git-core/templates/hooks/post-update.sample
/usr/share/git-core/templates/hooks/pre-applypatch.sample
/usr/share/git-core/templates/hooks/pre-commit.sample
/usr/share/git-core/templates/hooks/pre-push.sample
/usr/share/git-core/templates/hooks/pre-receive.sample
/usr/share/git-core/templates/hooks/update.sample
/usr/share/git-core/templates/info/exclude
/usr/share/gitweb/static/git-favicon.png
/usr/share/gitweb/static/git-logo.png
/usr/share/gitweb/static/gitweb.css
/usr/share/gitweb/static/gitweb.js

%files extras
%defattr(-,root,root,-)
/usr/bin/git-cvsserver
/usr/libexec/git-core/git-add--interactive
/usr/libexec/git-core/git-archimport
/usr/libexec/git-core/git-cvsexportcommit
/usr/libexec/git-core/git-cvsimport
/usr/libexec/git-core/git-cvsserver
/usr/libexec/git-core/git-instaweb
/usr/libexec/git-core/git-p4
/usr/libexec/git-core/git-request-pull
/usr/libexec/git-core/git-send-email
/usr/libexec/git-core/git-svn
/usr/share/git-core/templates/hooks/fsmonitor-watchman.sample
/usr/share/git-core/templates/hooks/pre-rebase.sample
/usr/share/git-core/templates/hooks/prepare-commit-msg.sample
/usr/share/gitweb/gitweb.cgi
/usr/share/perl5/FromCPAN/Error.pm
/usr/share/perl5/FromCPAN/Mail/Address.pm
/usr/share/perl5/Git.pm
/usr/share/perl5/Git/I18N.pm
/usr/share/perl5/Git/IndexInfo.pm
/usr/share/perl5/Git/LoadCPAN.pm
/usr/share/perl5/Git/LoadCPAN/Error.pm
/usr/share/perl5/Git/LoadCPAN/Mail/Address.pm
/usr/share/perl5/Git/Packet.pm
/usr/share/perl5/Git/SVN.pm
/usr/share/perl5/Git/SVN/Editor.pm
/usr/share/perl5/Git/SVN/Fetcher.pm
/usr/share/perl5/Git/SVN/GlobSpec.pm
/usr/share/perl5/Git/SVN/Log.pm
/usr/share/perl5/Git/SVN/Memoize/YAML.pm
/usr/share/perl5/Git/SVN/Migration.pm
/usr/share/perl5/Git/SVN/Prompt.pm
/usr/share/perl5/Git/SVN/Ra.pm
/usr/share/perl5/Git/SVN/Utils.pm

%files libexec
%defattr(-,root,root,-)
%exclude /usr/libexec/git-core/git-add--interactive
%exclude /usr/libexec/git-core/git-archimport
%exclude /usr/libexec/git-core/git-cvsexportcommit
%exclude /usr/libexec/git-core/git-cvsimport
%exclude /usr/libexec/git-core/git-cvsserver
%exclude /usr/libexec/git-core/git-gui
%exclude /usr/libexec/git-core/git-gui--askpass
%exclude /usr/libexec/git-core/git-instaweb
%exclude /usr/libexec/git-core/git-p4
%exclude /usr/libexec/git-core/git-request-pull
%exclude /usr/libexec/git-core/git-send-email
%exclude /usr/libexec/git-core/git-svn
/usr/libexec/git-core/git
/usr/libexec/git-core/git-add
/usr/libexec/git-core/git-am
/usr/libexec/git-core/git-annotate
/usr/libexec/git-core/git-apply
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
/usr/libexec/git-core/git-commit-graph
/usr/libexec/git-core/git-commit-tree
/usr/libexec/git-core/git-config
/usr/libexec/git-core/git-count-objects
/usr/libexec/git-core/git-credential
/usr/libexec/git-core/git-credential-cache
/usr/libexec/git-core/git-credential-cache--daemon
/usr/libexec/git-core/git-credential-store
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
/usr/libexec/git-core/git-hash-object
/usr/libexec/git-core/git-help
/usr/libexec/git-core/git-http-backend
/usr/libexec/git-core/git-http-fetch
/usr/libexec/git-core/git-http-push
/usr/libexec/git-core/git-imap-send
/usr/libexec/git-core/git-index-pack
/usr/libexec/git-core/git-init
/usr/libexec/git-core/git-init-db
/usr/libexec/git-core/git-interpret-trailers
/usr/libexec/git-core/git-legacy-rebase
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
/usr/libexec/git-core/git-multi-pack-index
/usr/libexec/git-core/git-mv
/usr/libexec/git-core/git-name-rev
/usr/libexec/git-core/git-notes
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
/usr/libexec/git-core/git-range-diff
/usr/libexec/git-core/git-read-tree
/usr/libexec/git-core/git-rebase
/usr/libexec/git-core/git-rebase--am
/usr/libexec/git-core/git-rebase--common
/usr/libexec/git-core/git-rebase--interactive
/usr/libexec/git-core/git-rebase--preserve-merges
/usr/libexec/git-core/git-receive-pack
/usr/libexec/git-core/git-reflog
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
/usr/libexec/git-core/git-rerere
/usr/libexec/git-core/git-reset
/usr/libexec/git-core/git-rev-list
/usr/libexec/git-core/git-rev-parse
/usr/libexec/git-core/git-revert
/usr/libexec/git-core/git-rm
/usr/libexec/git-core/git-send-pack
/usr/libexec/git-core/git-serve
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
/usr/libexec/git-core/git-submodule--helper
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
/usr/libexec/git-core/mergetools/examdiff
/usr/libexec/git-core/mergetools/guiffy
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/git/COPYING
/usr/share/package-licenses/git/compat_nedmalloc_License.txt
/usr/share/package-licenses/git/contrib_persistent-https_LICENSE
/usr/share/package-licenses/git/contrib_subtree_COPYING
/usr/share/package-licenses/git/sha1dc_LICENSE.txt
/usr/share/package-licenses/git/t_diff-lib_COPYING
/usr/share/package-licenses/git/vcs-svn_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/git-add.1
/usr/share/man/man1/git-am.1
/usr/share/man/man1/git-annotate.1
/usr/share/man/man1/git-apply.1
/usr/share/man/man1/git-archimport.1
/usr/share/man/man1/git-archive.1
/usr/share/man/man1/git-bisect.1
/usr/share/man/man1/git-blame.1
/usr/share/man/man1/git-branch.1
/usr/share/man/man1/git-bundle.1
/usr/share/man/man1/git-cat-file.1
/usr/share/man/man1/git-check-attr.1
/usr/share/man/man1/git-check-ignore.1
/usr/share/man/man1/git-check-mailmap.1
/usr/share/man/man1/git-check-ref-format.1
/usr/share/man/man1/git-checkout-index.1
/usr/share/man/man1/git-checkout.1
/usr/share/man/man1/git-cherry-pick.1
/usr/share/man/man1/git-cherry.1
/usr/share/man/man1/git-citool.1
/usr/share/man/man1/git-clean.1
/usr/share/man/man1/git-clone.1
/usr/share/man/man1/git-column.1
/usr/share/man/man1/git-commit-graph.1
/usr/share/man/man1/git-commit-tree.1
/usr/share/man/man1/git-commit.1
/usr/share/man/man1/git-config.1
/usr/share/man/man1/git-count-objects.1
/usr/share/man/man1/git-credential-cache--daemon.1
/usr/share/man/man1/git-credential-cache.1
/usr/share/man/man1/git-credential-store.1
/usr/share/man/man1/git-credential.1
/usr/share/man/man1/git-cvsexportcommit.1
/usr/share/man/man1/git-cvsimport.1
/usr/share/man/man1/git-cvsserver.1
/usr/share/man/man1/git-daemon.1
/usr/share/man/man1/git-describe.1
/usr/share/man/man1/git-diff-files.1
/usr/share/man/man1/git-diff-index.1
/usr/share/man/man1/git-diff-tree.1
/usr/share/man/man1/git-diff.1
/usr/share/man/man1/git-difftool.1
/usr/share/man/man1/git-fast-export.1
/usr/share/man/man1/git-fast-import.1
/usr/share/man/man1/git-fetch-pack.1
/usr/share/man/man1/git-fetch.1
/usr/share/man/man1/git-filter-branch.1
/usr/share/man/man1/git-fmt-merge-msg.1
/usr/share/man/man1/git-for-each-ref.1
/usr/share/man/man1/git-format-patch.1
/usr/share/man/man1/git-fsck-objects.1
/usr/share/man/man1/git-fsck.1
/usr/share/man/man1/git-gc.1
/usr/share/man/man1/git-get-tar-commit-id.1
/usr/share/man/man1/git-grep.1
/usr/share/man/man1/git-gui.1
/usr/share/man/man1/git-hash-object.1
/usr/share/man/man1/git-help.1
/usr/share/man/man1/git-http-backend.1
/usr/share/man/man1/git-http-fetch.1
/usr/share/man/man1/git-http-push.1
/usr/share/man/man1/git-imap-send.1
/usr/share/man/man1/git-index-pack.1
/usr/share/man/man1/git-init-db.1
/usr/share/man/man1/git-init.1
/usr/share/man/man1/git-instaweb.1
/usr/share/man/man1/git-interpret-trailers.1
/usr/share/man/man1/git-log.1
/usr/share/man/man1/git-ls-files.1
/usr/share/man/man1/git-ls-remote.1
/usr/share/man/man1/git-ls-tree.1
/usr/share/man/man1/git-mailinfo.1
/usr/share/man/man1/git-mailsplit.1
/usr/share/man/man1/git-merge-base.1
/usr/share/man/man1/git-merge-file.1
/usr/share/man/man1/git-merge-index.1
/usr/share/man/man1/git-merge-one-file.1
/usr/share/man/man1/git-merge-tree.1
/usr/share/man/man1/git-merge.1
/usr/share/man/man1/git-mergetool--lib.1
/usr/share/man/man1/git-mergetool.1
/usr/share/man/man1/git-mktag.1
/usr/share/man/man1/git-mktree.1
/usr/share/man/man1/git-multi-pack-index.1
/usr/share/man/man1/git-mv.1
/usr/share/man/man1/git-name-rev.1
/usr/share/man/man1/git-notes.1
/usr/share/man/man1/git-p4.1
/usr/share/man/man1/git-pack-objects.1
/usr/share/man/man1/git-pack-redundant.1
/usr/share/man/man1/git-pack-refs.1
/usr/share/man/man1/git-parse-remote.1
/usr/share/man/man1/git-patch-id.1
/usr/share/man/man1/git-prune-packed.1
/usr/share/man/man1/git-prune.1
/usr/share/man/man1/git-pull.1
/usr/share/man/man1/git-push.1
/usr/share/man/man1/git-quiltimport.1
/usr/share/man/man1/git-range-diff.1
/usr/share/man/man1/git-read-tree.1
/usr/share/man/man1/git-rebase.1
/usr/share/man/man1/git-receive-pack.1
/usr/share/man/man1/git-reflog.1
/usr/share/man/man1/git-remote-ext.1
/usr/share/man/man1/git-remote-fd.1
/usr/share/man/man1/git-remote-testgit.1
/usr/share/man/man1/git-remote.1
/usr/share/man/man1/git-repack.1
/usr/share/man/man1/git-replace.1
/usr/share/man/man1/git-request-pull.1
/usr/share/man/man1/git-rerere.1
/usr/share/man/man1/git-reset.1
/usr/share/man/man1/git-rev-list.1
/usr/share/man/man1/git-rev-parse.1
/usr/share/man/man1/git-revert.1
/usr/share/man/man1/git-rm.1
/usr/share/man/man1/git-send-email.1
/usr/share/man/man1/git-send-pack.1
/usr/share/man/man1/git-sh-i18n--envsubst.1
/usr/share/man/man1/git-sh-i18n.1
/usr/share/man/man1/git-sh-setup.1
/usr/share/man/man1/git-shell.1
/usr/share/man/man1/git-shortlog.1
/usr/share/man/man1/git-show-branch.1
/usr/share/man/man1/git-show-index.1
/usr/share/man/man1/git-show-ref.1
/usr/share/man/man1/git-show.1
/usr/share/man/man1/git-stage.1
/usr/share/man/man1/git-stash.1
/usr/share/man/man1/git-status.1
/usr/share/man/man1/git-stripspace.1
/usr/share/man/man1/git-submodule.1
/usr/share/man/man1/git-svn.1
/usr/share/man/man1/git-symbolic-ref.1
/usr/share/man/man1/git-tag.1
/usr/share/man/man1/git-unpack-file.1
/usr/share/man/man1/git-unpack-objects.1
/usr/share/man/man1/git-update-index.1
/usr/share/man/man1/git-update-ref.1
/usr/share/man/man1/git-update-server-info.1
/usr/share/man/man1/git-upload-archive.1
/usr/share/man/man1/git-upload-pack.1
/usr/share/man/man1/git-var.1
/usr/share/man/man1/git-verify-commit.1
/usr/share/man/man1/git-verify-pack.1
/usr/share/man/man1/git-verify-tag.1
/usr/share/man/man1/git-web--browse.1
/usr/share/man/man1/git-whatchanged.1
/usr/share/man/man1/git-worktree.1
/usr/share/man/man1/git-write-tree.1
/usr/share/man/man1/git.1
/usr/share/man/man1/gitk.1
/usr/share/man/man1/gitremote-helpers.1
/usr/share/man/man1/gitweb.1
/usr/share/man/man5/gitattributes.5
/usr/share/man/man5/githooks.5
/usr/share/man/man5/gitignore.5
/usr/share/man/man5/gitmodules.5
/usr/share/man/man5/gitrepository-layout.5
/usr/share/man/man5/gitweb.conf.5
/usr/share/man/man7/gitcli.7
/usr/share/man/man7/gitcore-tutorial.7
/usr/share/man/man7/gitcredentials.7
/usr/share/man/man7/gitcvs-migration.7
/usr/share/man/man7/gitdiffcore.7
/usr/share/man/man7/giteveryday.7
/usr/share/man/man7/gitglossary.7
/usr/share/man/man7/gitnamespaces.7
/usr/share/man/man7/gitrevisions.7
/usr/share/man/man7/gitsubmodules.7
/usr/share/man/man7/gittutorial-2.7
/usr/share/man/man7/gittutorial.7
/usr/share/man/man7/gitworkflows.7

%files locales -f git.lang
%defattr(-,root,root,-)

