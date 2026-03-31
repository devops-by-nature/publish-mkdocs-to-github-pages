"""MkDocs macros module — exposes project variables to documentation templates."""
import os
import xml.etree.ElementTree as ET


def define_env(env):
    """Define macro variables available in all MkDocs pages."""

    # Allow version to be overridden via environment variable.
    # Set DOCS_VERSION to the release tag when publishing to GitHub Pages,
    # or leave it unset to fall back to the version in pom.xml (e.g. for
    # snapshot/PR builds published to Netlify).
    version = os.environ.get("DOCS_VERSION")

    # Expose as {{ version }} macro in markdown pages
    env.variables["version"] = version
