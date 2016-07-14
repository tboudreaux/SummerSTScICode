from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[310.9965,-10.795192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_[L92b]_MarkA/sdB_[L92b]_MarkA_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_[L92b]_MarkA/sdB_[L92b]_MarkA_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
