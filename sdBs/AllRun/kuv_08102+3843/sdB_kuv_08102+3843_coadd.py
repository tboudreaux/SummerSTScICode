from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[123.374208,38.557531],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_08102+3843/sdB_kuv_08102+3843_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_08102+3843/sdB_kuv_08102+3843_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
