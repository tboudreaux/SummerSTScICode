from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.598042,28.834789],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pb_3524/sdB_pb_3524_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pb_3524/sdB_pb_3524_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
