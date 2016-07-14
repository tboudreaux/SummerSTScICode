from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[232.084667,10.508858],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1525+107/sdB_PG_1525+107_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1525+107/sdB_PG_1525+107_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
