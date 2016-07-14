from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[214.843667,29.781331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_3580/sdB_pb_3580_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_3580/sdB_pb_3580_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
