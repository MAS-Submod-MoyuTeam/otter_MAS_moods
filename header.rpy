init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Otter moods",
        description="New 'I feel' options.",
        version="1.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Otter moods",
            user_name="my-otter-self",
            repository_name="otter_MAS_moods",
            submod_dir="/Submods/Otter's moods",
            extraction_depth=3,
            redirected_files=(
                "README.md",
            )
        )
