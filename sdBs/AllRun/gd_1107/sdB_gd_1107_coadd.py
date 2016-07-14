from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.398042,-9.038781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_gd_1107/sdB_gd_1107_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_gd_1107/sdB_gd_1107_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
