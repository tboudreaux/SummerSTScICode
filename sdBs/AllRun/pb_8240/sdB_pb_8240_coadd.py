from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[6.762042,-7.853489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_8240/sdB_pb_8240_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_8240/sdB_pb_8240_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
