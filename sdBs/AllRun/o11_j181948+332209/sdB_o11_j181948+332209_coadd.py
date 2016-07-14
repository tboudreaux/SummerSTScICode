from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[274.95,33.369167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j181948+332209/sdB_o11_j181948+332209_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j181948+332209/sdB_o11_j181948+332209_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
