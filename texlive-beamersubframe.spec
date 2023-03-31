Name:		texlive-beamersubframe
Version:	23510
Release:	2
Summary:	Reorder frames in the PDF file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beamersubframe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a method to reorder frames in the PDF file
without reordering the source. Its principal use is to embed or
append frames with details on some subject. The author
describes the package as "experimental".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
