from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[324.794167,-46.097639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hd_205805/sdB_hd_205805_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hd_205805/sdB_hd_205805_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
