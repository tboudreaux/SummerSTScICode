from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[80.183292,-61.497275],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J05207-6129/sdB_GALEX_J05207-6129_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J05207-6129/sdB_GALEX_J05207-6129_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
