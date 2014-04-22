MAIN_OPTIONS = ['lmnp','a','mnp','e','m','e','lnp','qrsu']

words = []
bags = []


def options_with(options):
    if len(options) == 1:
        return [c for c in options[0]]
    cumulative_options = []
    for c in options[0]:
        if len(options[0]) == 7:
        cumulative_options.extend([c + x for x in options_with(options[1:])])
    return cumulative_options


bags = [{c : x.count(c) for c in x} for x in options_with(options)]
removed = 0
for i in range(len(bags)):
    c_bag = bags[i-removed]
    for b in bags[i-removed+1:]:
        all_in = True
        for x in b.keys():
            if x not in c_bag or c_bag[x] != b[x]:
                all_in = False
                break
        if all_in:
            del bags[i-removed]
            removed += 1
            break
final = [''.join([c * b[c] for c in b.keys()]) for b in bags]
print len(final)
print '\n'.join(final)
