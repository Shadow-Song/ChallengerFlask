'''
This file generated the build configurations for the array builds
'''

from itertools import product

if "builds" not in config:
    config["builds"] = {}

# Expand variables in subsamples for named builds.
for build_name, build_params in config["builds"].items():
    subsamples = build_params.pop("subsamples", None)

    if subsamples is not None:
        tmp = {}
        for subsample in subsamples:
            tmp[subsample] = {}
            tmp[subsample]["filters"] = subsamples[subsample]["filters"].format(**build_params)
            if "priorities" in subsamples[subsample]:
                tmp[subsample]["priorities"] = subsamples[subsample]["priorities"].format(**build_params)
        config['builds'][build_name] = {'subsamples': tmp}
        config['builds'][build_name].update(build_params)

# Expand array builds.
for array_build in config.get("array-builds", {}).values():
    patterns = array_build["patterns"]
    subsamples = array_build["subsamples"]

    for build_vars in product(*patterns.values()):
        # e.g. center:cdc, assay:hi
        build_params = {k:v for k,v in zip(patterns.keys(), build_vars)}
        # additional parameters like size:4000
        build_params.update({k:eval(v.format(**build_params)) for k,v in array_build.get('subsampling_parameters',{}).items()})

        build_name = array_build["build_name"].format(**build_params)
        for k,v in array_build.get("build_params",{}).items():
            if isinstance(v, str):
                build_params[k] = v.format(**build_params)
            elif k == "titer_collections":
                # Allow expansion of build parameters in titer collection
                # attributes like data path and title.
                titer_collections = []
                for original_titer_collection in v:
                    titer_collection = original_titer_collection.copy()
                    for titer_collection_key, titer_collection_value in titer_collection.items():
                        titer_collection[titer_collection_key] = titer_collection_value.format(**build_params)

                    titer_collections.append(titer_collection)

                build_params[k] = titer_collections
            else:
                build_params[k] = v

        tmp = {}
        for subsample in subsamples:
            tmp[subsample] = {}
            tmp[subsample]["filters"] = subsamples[subsample]["filters"].format(**build_params)
            if "priorities" in subsamples[subsample]:
                tmp[subsample]["priorities"] = subsamples[subsample]["priorities"].format(**build_params)
        config['builds'][build_name] = {'subsamples': tmp}
        config['builds'][build_name].update(build_params)

        if("auspice_config" in array_build):
            config['builds'][build_name]['auspice_config'] = array_build["auspice_config"]

        if("description" in array_build):
            config['builds'][build_name]['description'] = array_build["description"]

        if("deploy_urls" in array_build):
            deploy_urls = array_build["deploy_urls"]
            config['builds'][build_name]['deploy_urls'] = set([deploy_urls] if type(deploy_urls)==str else deploy_urls)

    # for b in config["builds"]:
    #     print(b, config["builds"][b])
