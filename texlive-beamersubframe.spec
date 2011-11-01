Name:		texlive-beamersubframe
Version:	0.2
Release:	1
Summary:	Reorder frames in the PDF file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beamersubframe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a method to reorder frames in the PDF file
without reordering the source. Its principal use is to embed or
append frames with details on some subject. The author
describes the package as "experimental".

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamersubframe/beamersubframe.sty
%doc %{_texmfdistdir}/doc/latex/beamersubframe/README
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.svg
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.svg
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/bsf-example.tex
#- source
%doc %{_texmfdistdir}/source/latex/beamersubframe/beamersubframe.dtx
%doc %{_texmfdistdir}/source/latex/beamersubframe/beamersubframe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
