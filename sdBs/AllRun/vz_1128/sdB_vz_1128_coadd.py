from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[205.570042,28.433528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_vz_1128/sdB_vz_1128_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_vz_1128/sdB_vz_1128_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
