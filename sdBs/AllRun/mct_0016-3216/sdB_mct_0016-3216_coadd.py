from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[4.852083,-31.998028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_mct_0016-3216/sdB_mct_0016-3216_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_mct_0016-3216/sdB_mct_0016-3216_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
