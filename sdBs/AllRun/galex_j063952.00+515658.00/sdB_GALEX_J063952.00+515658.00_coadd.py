from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[99.966667,51.949444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J063952.00+515658.00/sdB_GALEX_J063952.00+515658.00_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J063952.00+515658.00/sdB_GALEX_J063952.00+515658.00_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
