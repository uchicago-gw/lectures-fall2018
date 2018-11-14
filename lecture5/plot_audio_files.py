#!/usr/bin/env python

"""make plots of spectra of snaps and claps
"""




fs, data = wavfile.read(args.source)
N, ndim = data.shape

w = filters.tukey(N, alpha=args.tukey_alpha)

fig = plt.figure()
ax = fig.gca()

f = np.fft.fftshift(np.fft.fftfreq(N, d=1./fs))
fmax = min(args.fmax, 0.5*fs)
truth = np.abs(f)<=fmax
for d in range(ndim):
    ax.plot(f[truth], np.abs(np.fft.fftshift(np.fft.fft(data[:,d]*w)))[truth], alpha=0.5)

ax.set_xlabel('frequency')
ax.set_yscale('log')
ax.set_xlim(xmin=0, xmax=fmax)

if args.verbose:
    print('saving: '+target)
fig.savefig(target)
plt.close(fig)
