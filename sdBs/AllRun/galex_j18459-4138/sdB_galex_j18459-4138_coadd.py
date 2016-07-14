from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[281.4995,-41.640797],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j18459-4138/sdB_galex_j18459-4138_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j18459-4138/sdB_galex_j18459-4138_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
