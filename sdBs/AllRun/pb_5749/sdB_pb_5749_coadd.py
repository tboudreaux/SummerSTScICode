from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[1.908083,0.667967],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_5749/sdB_pb_5749_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_5749/sdB_pb_5749_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
