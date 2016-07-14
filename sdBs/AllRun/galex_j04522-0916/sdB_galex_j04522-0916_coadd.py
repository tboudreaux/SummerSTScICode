from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[73.055083,-9.276122],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j04522-0916/sdB_galex_j04522-0916_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j04522-0916/sdB_galex_j04522-0916_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
