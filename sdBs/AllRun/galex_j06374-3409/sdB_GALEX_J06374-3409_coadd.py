from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[99.369375,-34.156458],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J06374-3409/sdB_GALEX_J06374-3409_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J06374-3409/sdB_GALEX_J06374-3409_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
