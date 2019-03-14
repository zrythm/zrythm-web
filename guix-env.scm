;;; This file is part of GNUnet.
;;; Copyright (C) 2017, 2018 GNUnet e.V.
;;;
;;; GNUnet is free software; you can redistribute it and/or modify
;;; it under the terms of the GNU General Public License as published
;;; by the Free Software Foundation; either version 3, or (at your
;;; option) any later version.
;;;
;;; GNUnet is distributed in the hope that it will be useful, but
;;; WITHOUT ANY WARRANTY; without even the implied warranty of
;;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
;;; General Public License for more details.
;;;
;;; You should have received a copy of the GNU General Public License
;;; along with GNUnet; see the file COPYING.  If not, write to the
;;; Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
;;; Boston, MA 02110-1301, USA.

(use-modules
 (ice-9 popen)
 (ice-9 match)
 (ice-9 rdelim)
 (guix packages)
 (guix build-system gnu)
 (guix gexp)
 ((guix build utils) #:select (with-directory-excursion))
 (guix git-download)
 (guix utils) ; current-source-directory
 (gnu packages)
 (gnu packages aidc)
 (gnu packages autotools)
 (gnu packages backup)
 (gnu packages base)
 (gnu packages compression)
 (gnu packages curl)
 (gnu packages check)
 (gnu packages databases)
 (gnu packages file)
 (gnu packages gettext)
 (gnu packages less)
 (gnu packages glib)
 (gnu packages gnome)
 (gnu packages gnunet)
 (gnu packages gnupg)
 (gnu packages gnuzilla)
 (gnu packages groff)
 (gnu packages gstreamer)
 (gnu packages gtk)
 (gnu packages guile)
 (gnu packages image)
 (gnu packages image-viewers)
 (gnu packages libidn)
 (gnu packages libunistring)
 (gnu packages linux)
 (gnu packages maths)
 (gnu packages multiprecision)
 (gnu packages perl)
 (gnu packages pkg-config)
 (gnu packages pulseaudio)
 (gnu packages python)
 (gnu packages tex)
 (gnu packages texinfo)
 (gnu packages tex)
 (gnu packages tls)
 (gnu packages upnp)
 (gnu packages openstack)
 (gnu packages video)
 (gnu packages web)
 (gnu packages version-control)
 (gnu packages xiph)
 ((guix licenses) #:prefix license:))

(define %source-dir (dirname (current-filename)))

(define gnunet-website-git
  (let* ((revision "2"))
    (package
      (name "gnunet-website-git")
      (version (string-append "0.0.0-" revision "." "dev"))
      (source
       (local-file %source-dir
                   #:recursive? #t))
      ;; FIXME: Switch to python-build-system!
      (build-system gnu-build-system)
      (inputs
       `(("python-jinja2" ,python-jinja2)
         ("python-babel" ,python-babel)
         ("python-pylint" ,python-pylint)
         ("python-oslo.i18n" ,python-oslo.i18n)
         ("python-future" ,python-future)
         ("gettext-minimal" ,gettext-minimal)
         ("python" ,python)
         ("coreutils" ,coreutils)
         ("which" ,which)
         ("less" ,less)
         ("git" ,git)
         ("automake" ,automake)
         ("autoconf" ,autoconf-wrapper)))
      (arguments
       `(#:phases
         (modify-phases %standard-phases
           (add-after 'unpack 'po-file-chmod
             (lambda _
               ;; Make sure 'msgmerge' can modify the PO files.
               (for-each (lambda (po)
                           (chmod po #o666))
                         (find-files "." "\\.po$"))))
           ;; (replace 'configure
           ;;   (lambda* (#:key outputs inputs #:allow-other-keys)
           ;;     (let ((pystore (assoc-ref inputs "python"))
           ;;           (pyver ,(version-major+minor (package-version python))))
           ;;       (substitute* "Makefile"
           ;;         (("env PYTHONPATH=\".\"")
           ;;          (string-append
           ;;           "env PYTHONPATH=\""
           ;;           (getenv "PYTHONPATH")
           ;;           ":"
           ;;           "."
           ;;           "\""))))))
           ;; FIXME: Implement small testsuite.
           (delete 'check))))
      (synopsis "GNUnet website generation")
      (description
       "GNUnet-website builds the website.")
      (license #f)
      (home-page "https://gnunet.org"))))

gnunet-website-git
