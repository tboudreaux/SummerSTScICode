from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[305.1135,7.070683],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J20204+0704/sdB_GALEX_J20204+0704_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J20204+0704/sdB_GALEX_J20204+0704_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
