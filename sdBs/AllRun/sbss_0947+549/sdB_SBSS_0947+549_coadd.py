from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.670667,54.691719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_0947+549/sdB_SBSS_0947+549_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_0947+549/sdB_SBSS_0947+549_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
