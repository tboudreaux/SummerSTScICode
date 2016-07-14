from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[353.644542,-1.326342],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_5450/sdB_pb_5450_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_5450/sdB_pb_5450_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
