from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.026667,9.272244],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J09121+0916/sdB_GALEX_J09121+0916_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J09121+0916/sdB_GALEX_J09121+0916_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
