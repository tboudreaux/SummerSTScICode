from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[344.587167,-7.900828],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_7409/sdB_pb_7409_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_7409/sdB_pb_7409_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
