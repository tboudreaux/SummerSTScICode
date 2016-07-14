from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[0.095125,0.109931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_5670/sdB_pb_5670_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_5670/sdB_pb_5670_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
